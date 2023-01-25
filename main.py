import tkinter as tk


def calculate():
    participation = float(entry1.get())
    alc = float(entry2.get())
    midterm_exam = float(entry3.get())

    overall_average = participation + alc + midterm_exam

    if overall_average > 1350:
        label4.configure(text="You don't even have to take the final exam. Congrats!")
    else:
        final_score_needed = (1350 - overall_average)
        label4.configure(
            text="You need to score " + str(final_score_needed) + " points on the final to pass the class.")
        label5.configure(
            text=" That is equivalent to a " + str(round((final_score_needed / 600) * 100, 2)) + "% on the final.")


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

root.mainloop()
