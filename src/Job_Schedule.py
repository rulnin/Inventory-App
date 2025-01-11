import time
import schedule
import papermill as pm

def jobs():
    start: float = time.time()
    print('Running Inventory Algorithm Notebook...')
    # Jalankan notebook menggunakan papermill
    pm.execute_notebook(
        'Inventory Algorithm.ipynb',  # Notebook sumber
        'Inventory Algorithm Output.ipynb'  # Notebook output
    )
    end: float = time.time()
    print(f"Time Estimated {end - start} seconds")

# Scheduling setiap 2 menit
schedule.every(2).minutes.do(jobs)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
