import os
import time


def format_timing(seconds: float) -> str:
    """
    creates minutes:seconds out of a float
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst):
    """
    imitating basic behavior of tqdm
    creates a progress bar and ETA timing
    """
    terminal_width = os.get_terminal_size().columns
    start_time = time.time()
    total = len(lst)

    for i, item in enumerate(lst, start=1):

        # percentage
        percent = int(i / total * 100)

        # counter
        counting = str(i) + "/" + str(total)
        counting_len = (len(str(total))) * 2 + 1

        # timing
        time_diff = time.time() - start_time
        rate = i / time_diff if time_diff > 0 else 0
        eta = (total - i) / rate if rate > 0 else 0
        timing = (
            f"[{format_timing(time_diff)}<{format_timing(eta)}, "
            f"{rate:.2f}it/s]"
        )

        progress_bar_len = terminal_width - counting_len - len(timing) - 8
        if progress_bar_len <= 0:
            progress_bar_len = 1

        # progress bar
        fill = "█"
        empty = " "
        filled_len = int(progress_bar_len * (percent / 100))
        empty_len = progress_bar_len - filled_len
        progress_bar = filled_len * fill + empty_len * empty

        display = (
            f"\r{percent:>3}%|{progress_bar}| "
            f"{counting:>{counting_len}} {timing}"
        )
        if len(display) > terminal_width:
            display = display[:terminal_width]

        print(display, end="", flush=True)

        yield item


# items = list(range(333))
# for item in ft_tqdm(items):
#     time.sleep(0.005)
# print()

# import inspect
#
# def see_inside():
#     my_iterator = ft_tqdm(range(13))
#
#     while my_iterator:
#         first_item = next(my_iterator)
#
#         # 'gi_frame' is the saved stack frame
#         # 'f_locals' is the dictionary of all local variables
#         saved_variables = my_iterator.gi_frame.f_locals
#
#         print(f"Current Index (i): {saved_variables['i']}")
#         print(f"Total Items: {saved_variables['total']}")
#         print(f"Start Time: {saved_variables['start_time']}")
