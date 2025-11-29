"""
Asynchronous operations module with asyncio and aiohttp.
"""

import asyncio
import aiohttp
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """
    Fetch a single URL asynchronously.
    
    Args:
        session: aiohttp client session
        url: URL to fetch
        
    Returns:
        Dictionary with URL and response data
    """
    try:
        async with session.get(url) as response:
            data = await response.text()
            logger.info(f"Fetched {url} - Status: {response.status}")
            return {
                'url': url,
                'status': response.status,
                'content_length': len(data),
                'success': True
            }
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return {
            'url': url,
            'error': str(e),
            'success': False
        }


async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch multiple URLs concurrently.
    
    Args:
        urls: List of URLs to fetch
        
    Returns:
        List of results for each URL
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def process_data_async(items: List[Any], delay: float = 0.1) -> List[Any]:
    """
    Process data asynchronously with simulated delay.
    
    Args:
        items: Items to process
        delay: Delay between processing items
        
    Returns:
        Processed items
    """
    processed = []
    
    for item in items:
        await asyncio.sleep(delay)
        processed_item = {
            'original': item,
            'processed': True,
            'timestamp': asyncio.get_event_loop().time()
        }
        processed.append(processed_item)
        logger.debug(f"Processed item: {item}")
    
    return processed


async def async_task_runner(num_tasks: int = 5):
    """
    Run multiple async tasks concurrently.
    
    Args:
        num_tasks: Number of tasks to run
    """
    async def worker(task_id: int):
        """Worker coroutine."""
        logger.info(f"Task {task_id} starting...")
        await asyncio.sleep(0.5)
        logger.info(f"Task {task_id} completed")
        return f"Result from task {task_id}"
    
    tasks = [worker(i) for i in range(num_tasks)]
    results = await asyncio.gather(*tasks)
    
    logger.info(f"All {num_tasks} tasks completed")
    return results


class AsyncDataProcessor:
    """Async data processor with queue support."""
    
    def __init__(self, max_workers: int = 3):
        """
        Initialize async processor.
        
        Args:
            max_workers: Maximum concurrent workers
        """
        self.max_workers = max_workers
        self.queue = asyncio.Queue()
        self.results = []
    
    async def worker(self, worker_id: int):
        """
        Worker that processes items from the queue.
        
        Args:
            worker_id: Worker identifier
        """
        while True:
            try:
                item = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                logger.info(f"Worker {worker_id} processing: {item}")
                
                # Simulate processing
                await asyncio.sleep(0.2)
                result = {'item': item, 'worker': worker_id, 'status': 'processed'}
                self.results.append(result)
                
                self.queue.task_done()
            except asyncio.TimeoutError:
                break
            except Exception as e:
                logger.error(f"Worker {worker_id} error: {e}")
                self.queue.task_done()
    
    async def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        """
        Process a batch of items with multiple workers.
        
        Args:
            items: Items to process
            
        Returns:
            List of processing results
        """
        # Add items to queue
        for item in items:
            await self.queue.put(item)
        
        # Create workers
        workers = [asyncio.create_task(self.worker(i)) for i in range(self.max_workers)]
        
        # Wait for queue to be processed
        await self.queue.join()
        
        # Cancel workers
        for worker in workers:
            worker.cancel()
        
        logger.info(f"Processed {len(self.results)} items")
        return self.results


def run_async_example():
    """Run async examples."""
    print("\n=== Async Operations Examples ===\n")
    
    # Example 1: Process data async
    print("1. Processing data asynchronously...")
    items = ['item1', 'item2', 'item3', 'item4', 'item5']
    results = asyncio.run(process_data_async(items, delay=0.05))
    print(f"   Processed {len(results)} items")
    
    # Example 2: Run concurrent tasks
    print("\n2. Running concurrent tasks...")
    task_results = asyncio.run(async_task_runner(3))
    for result in task_results:
        print(f"   {result}")
    
    # Example 3: Batch processing with queue
    print("\n3. Batch processing with workers...")
    processor = AsyncDataProcessor(max_workers=2)
    batch_items = [f"task_{i}" for i in range(10)]
    batch_results = asyncio.run(processor.process_batch(batch_items))
    print(f"   Processed {len(batch_results)} items with workers")
    
    print("\n=== Async Examples Completed ===\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_async_example()
