import tkinter as tk


def calculate():
    participation = float(entry1.get())
    a_l_c = float(entry2.get())
    midterm_exam = float(entry3.get())

    overall_average = participation + a_l_c + midterm_exam

    points_needed_for_A = 1800 - overall_average
    points_needed_for_B = 1600 - overall_average
    points_needed_for_C = 1400 - overall_average

    display_points(points_needed_for_A, points_needed_for_B, points_needed_for_C)


def display_points(points_needed_for_A, points_needed_for_B, points_needed_for_C):
    percentage_needed_for_A = round((points_needed_for_A / 600) * 100, 1)
    percentage_needed_for_B = round((points_needed_for_B / 600) * 100, 1)
    percentage_needed_for_C = round((points_needed_for_C / 600) * 100, 1)

    label6.configure(text="You need " + str(points_needed_for_A) + " more points to get an 'A' in the class."
                                                                   " That is equivalent to a " + str(
        percentage_needed_for_A) + "% on the final exam.")

    label7.configure(text="You need " + str(points_needed_for_B) + " more points to get a 'B' in the class."
                                                                   " That is equivalent to a " + str(
        percentage_needed_for_B) + "% on the final exam.")

    label8.configure(text="You need " + str(points_needed_for_C) + " more points to get a 'C' in the class."
                                                                   " That is equivalent to a " + str(
        percentage_needed_for_C) + "% on the final exam.")


root = tk.Tk()
root.title("Final Exam Calculator")

label1 = tk.Label(root, text="Enter your overall participation score (0-100):")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter your overall assignments, labs, and quizzes score (0-900):")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Enter your midterm exam score (0-400):")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

button1 = tk.Button(root, text="Calculate", command=calculate)
button1.grid(row=3, column=0)

label4 = tk.Label(root, text="")
label4.grid(row=4, column=0)

label5 = tk.Label(root, text="")
label5.grid(row=5, column=0)

label6 = tk.Label(root, text="")
label6.grid(row=6, column=0)

label7 = tk.Label(root, text="")
label7.grid(row=7, column=0)

label8 = tk.Label(root, text="")
label8.grid(row=8, column=0)

root.mainloop()
