from linked_queue import LinkedQueue
# Printing Jobs

printing_queue = LinkedQueue()

def new_job(job):
    printing_queue.enqueue(job)

def process_job():
    if not printing_queue.is_empty():
        print(f"Processing job: {printing_queue.dequeue()}")
    else:
        print("All jobs are finish!")

job1 = "Print document123.pdf"
job2 = "Print gsg.pdf"
job3 = "Print data_structures.pdf"

new_job(job1)
new_job(job2)
print(printing_queue)
process_job()
new_job(job3)
process_job()
print(printing_queue)
process_job()
print(printing_queue)




