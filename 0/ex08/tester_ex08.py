from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in tqdm(range(333)):
    sleep(0.005)
print()
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# )
# ft_gen = ft_tqdm(data)
#
# sys.stdout.write("\033[1A")
# sys.stdout.flush()
# try:
#     while True:
#         item1 = next(tqdm_gen)
#         sys.stdout.flush()
#
#         # Move cursor down
#         sys.stdout.write("\033[B")
#         sys.stdout.flush()
#         item2 = next(ft_gen)
#
#         # Move cursor up
#         sys.stdout.write("\033[A")
#         sys.stdout.flush()
#         time.sleep(0.05)
#
# except StopIteration:
#     pass
#
# print("\n\nDone!")
