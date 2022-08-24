from tkinter import *
from main_code import database_reader as data


def main():
    global stats
    stats = Statistics()
    stats.statistics_window()


# Updates the statistics
def update(score, timestamp):
    path = data.get_path()
    statistics_file = open(path + '/statistics.txt', 'r+')
    statistics_file_read = statistics_file.read().splitlines()
    record_candidate = timestamp + ' ' + str(score)
    scores_list = []
    for i in range(0, len(statistics_file_read)):
        scores_list.append(int(statistics_file_read[i].split(' ').pop()))

    # Adds the score to the list
    if len(scores_list) == 10:
        if score > min(scores_list) and scores_list != []:
            statistics_file_read[scores_list.index(min(scores_list))] = record_candidate
            statistics_file.close()
            statistics_file = open(path + '/statistics.txt', 'w')
            for line in statistics_file_read:
                    statistics_file.write(line + '\n')
            statistics_file.flush()
    else:
        statistics_file.write(record_candidate + '\n')


class Statistics:
    def statistics_window(self):
        stats_window = Tk()
        stats_frame = Frame(stats_window, width=1, height=1, bg="white")
        stats_frame.pack()
        stats_window.title("Know your elements")

        # Gets the requested values of the height and width.
        window_width = stats_window.winfo_reqwidth()
        window_height = stats_window.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(stats_window.winfo_screenwidth() / 4.5 - window_width)
        position_down = int(stats_window.winfo_screenheight() / 2.3 - window_height)

        # Positions the window in the center of the page.
        stats_window.geometry("+{}+{}".format(position_right, position_down))

        # Adding a label with a name
        statistics_name = Label(stats_frame, text="Time Trial Statistics", fg="black", bg="white")
        statistics_name.grid(columnspan=5, row=0)
        statistics_name.config(font=("Calibri", 17))

        ranking_name = Label(stats_frame, text="Ranking", fg="black", bg="gray")
        ranking_name.grid(column=0, row=1, sticky=NSEW)
        ranking_name.config(font=("Calibri", 15))

        score_name = Label(stats_frame, text=" Score ", fg="black", bg="gray")
        score_name.grid(column=1, row=1, sticky=NSEW)
        score_name.config(font=("Calibri", 15))

        timestamp_name = Label(stats_frame, text="   Timestamp   ", fg="black", bg="gray")
        timestamp_name.grid(column=2, row=1, sticky=NSEW)
        timestamp_name.config(font=("Calibri", 15))

        close_name = Button(stats_frame, text="Close", command=lambda: stats_window.destroy(), fg="red4", bg="grey40")
        close_name.grid(columnspan=1, row=13, column=0, sticky=NSEW)
        close_name.config(font=("Calibri", 17))

        clear_name = Button(stats_frame, text="Clear Statistics", command=lambda: self.clear(stats_window), fg="black", bg="red3")
        clear_name.grid(columnspan=4, row=13, column=1, sticky=NSEW)
        clear_name.config(font=("Calibri", 17))

        for number in range(1, 11):
            globals()['number%s' % number] = Label(stats_frame, text=str(number) + '.', fg="black", bg="lightgrey")
            globals()['number%s' % number].config(font=("Calibri", 12))
            globals()['number%s' % number].grid(column=0, row=number + 1, sticky=NSEW)

        # Score sorting
        path = data.get_path()
        statistics_file_read = open(path + '/statistics.txt').read().splitlines()
        changes = 1
        while changes != 0:
            changes = 0
            for i in range(0, len(statistics_file_read)):
                score_current = int(statistics_file_read[i].split(' ').pop())
                score_next = -1
                if i != len(statistics_file_read) - 1:
                    score_next = int(statistics_file_read[i+1].split(' ').pop())

                if score_current < score_next:
                    stored = statistics_file_read[i+1]
                    statistics_file_read[i+1] = statistics_file_read[i]
                    statistics_file_read[i] = stored
                    changes += 1
        statistics_file_read_sorted = statistics_file_read

        for record in statistics_file_read_sorted:
            record_split = record.split(' ')
            score = record_split[-1]
            record_split.pop()
            timestamp = ' '.join(record_split)
            record_number = statistics_file_read.index(record) + 1
            if not record:
                globals()['score%s' % record_number] = Label(stats_frame, text="", fg="black", bg="white")
                globals()['score%s' % record_number].config(font=("Calibri", 15))
                globals()['score%s' % record_number].grid(column=1, row=record_number + 1, sticky=NSEW)
                globals()['record%s' % record_number] = Label(stats_frame, text="", fg="black", bg="white")
                globals()['record%s' % record_number].config(font=("Calibri", 15))
                globals()['record%s' % record_number].grid(column=2, row=record_number + 1, sticky=NSEW)
            else:
                globals()['score%s' % record_number] = Label(stats_frame, text=score, fg="black", bg="white")
                globals()['score%s' % record_number].config(font=("Calibri", 15))
                globals()['score%s' % record_number].grid(column=1, row=record_number + 1, sticky=NSEW)
                globals()['record%s' % record_number] = Label(stats_frame, text=timestamp, fg="black", bg="white")
                globals()['record%s' % record_number].config(font=("Calibri", 15))
                globals()['record%s' % record_number].grid(column=2, row=record_number + 1, sticky=NSEW)

    def clear(self, stats_window):
        path = data.get_path()
        statistics_file = open(path + '/statistics.txt', 'r+')
        statistics_file.truncate(0)
        statistics_file.seek(0)
        statistics_file.flush()
        stats_window.destroy()
        main()