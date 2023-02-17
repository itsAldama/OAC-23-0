import asyncio
import time


async def count():
    print("Uno")
    await asyncio.sleep(1)
    print("Dos")


async def main():
    await asyncio.gather(*(count() for _ in range(3)))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()
    print(f"Tiempo de ejecución asincrono: {fin - inicio:0.4f} segundos")