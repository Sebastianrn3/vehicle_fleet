from tkinter import *

accounting_source = {
    "revenues":  {"FASTTRACK STIPENDIJA":100},
    "expenses": {"NUPIRKTAS KEFYRAS":77},
}

def enter_revenues():
    key, value = entry.get().split("=")
    accounting_source["revenues"][key] = value
    label_output["text"] = f"Įrašytos pajamos: {key}, +{value}"

def enter_expenses():
    key, value = entry.get().split("=")
    accounting_source["expenses"][key] = value
    label_output["text"] = f"Įrašytos išlaidos: {key}, -{value}"

def get_balance():
    balance = sum(accounting_source["revenues"].values()) - sum(accounting_source["expenses"].values())
    label_output["text"] = f"Balansas: {balance}"

def get_report():
    total_expenses = sum(accounting_source["expenses"].values())
    total_revenues = sum(accounting_source["revenues"].values())

    revenues_report = ""
    for key in accounting_source["revenues"].keys():
        revenues_report += f"{key}, {accounting_source["revenues"].get(key)}\n"
    revenues_report += f"Viso gauta: {total_revenues}\n"

    expenses_report = ""
    for key in accounting_source["expenses"].keys():
        expenses_report += f"{key}, {accounting_source["expenses"].get(key)}\n"
    expenses_report += f"Viso išleista: {total_expenses}\n"

    label_output["text"] = f"""
    BIUDŽETO ATASKAITA:\n***\n
    PAJAMOS:\n{revenues_report}\n***\n
    IŠLAIDOS:\n{expenses_report}\n******\n
    Balansas: {total_revenues-total_expenses}
    """

root = Tk()
root.title("Mano biudžetas")
root.geometry("600x700")

Label(text=f"Sveiki! Duomenis suvedami formatu: OPERACIJOS PAVADINIMAS = SUMA", font=("", 11)).pack()

Label(text="Užregistruoti pajamas arba išlaidas:").pack()
entry = Entry()
entry.pack(fill=X, ipady=10)

Button(text="Įrašyti kaip pajamas", command=enter_revenues).pack(fill=X, ipady=10)
Button(text="Įrašyti kaip išlaidas", command=enter_expenses).pack(fill=X, ipady=10)
Button(text="Sužinoti balansą", command=get_balance).pack(fill=X, ipady=10)
Button(text="Gauti ataskaitą", command=get_report).pack(fill=X, ipady=10)

label_output = Label()
label_output.pack(fill=X, ipady=20)

root.attributes("-alpha", 0.95)
root.attributes("-toolwindow", True)

root.mainloop()

#nesigavo apjungti į vieną funkciją:
# def add_transaction(entry, category):
#     user_input = entry.get().split("=")
#     key = user_input[0]
#     value = abs(int(user_input[1]))
#     accounting_source[category][key] = value
#     # if category == "expenses":
#     #     value = -value
#     label_output["text"] = f"Įrašyta tranzakcija: {key}, {value}"

#v0.1
# from tkinter import *
#
# revenues = {"FASTTRACK STIPENDIJA": 100}
# expenses = {"NUPIRKTAS KEFYRAS": 77}
#
#
# def enter_revenues():
#     input = entry_revenues.get().split("=")
#     key = input[0]
#     value = int(input[1])
#     revenues[key] = value
#     label_output["text"] = f"Įrašytos pajamos: {key}, +{value}"
#
#
# def enter_expenses():
#     input = entry_expenses.get().split("=")
#     key = input[0]
#     value = abs(int(input[1]))
#     expenses[key] = value
#     label_output["text"] = f"Įrašytos išlaidos: {key}, -{value}"
#
#
# def get_balance():
#     label_output["text"] = f"Balansas: {sum(revenues.values()) - sum(expenses.values())}"
#
#
# def get_report():
#     balance = sum(revenues.values()) - sum(expenses.values())
#
#     revenues_report = ""
#     for key in revenues.keys():
#         revenues_report += f"{key}, {revenues.get(key)}\n"
#
#     expenses_report = ""
#     for key in expenses.keys():
#         expenses_report += f"{key}, {expenses.get(key)}\n"
#
#     label_output["text"] = f"""
#     BIUDŽETO ATASKAITA:
#     ***
#     PAJAMOS:
#     {revenues_report}
#
#     IŠLAIDOS:
#     {expenses_report}
#     ***
#     Balansas: {sum(revenues.values()) - sum(expenses.values())}
#     """
#
#
# root = Tk()
# root.title("Mano biudžetas")
# root.geometry("600x700")
#
# label_greeting = Label(text="""
# Laba diena! Duomenis suvedami formatu: /OPERACIJOS PAVADINIMAS = SUMA/
#
# Pvz: FASTRACK STIPENDIJA = 100
# """)
# label_greeting.pack()
#
# label_revenues = Label(text="Leidžiame jums įvesti pajamas:")
# label_revenues.pack()
#
# entry_revenues = Entry()
# entry_revenues.pack(fill=X, ipady=10)
#
# button_revenues = Button(text="Įrašyti pajamas", command=enter_revenues)
# button_revenues.pack(fill=X, ipady=10)
# #
#
# label_expenses = Label(text="Taip pat leidžiame ir įvesti išlaidas:")
# label_expenses.pack()
#
# entry_expenses = Entry()
# entry_expenses.pack(fill=X, ipady=10)
#
# button_expenses = Button(text="Įrašyti išlaidas", command=enter_expenses)
# button_expenses.pack(fill=X, ipady=10)
#
# button_balance = Button(text="Sužinoti balansą", command=get_balance)
# button_balance.pack(fill=X, ipady=10)
#
# button_report = Button(text="Gauti ataskaitą", command=get_report)
# button_report.pack(fill=X, ipady=10)
#
# label_output = Label()
# label_output.pack(fill=X, ipady=20)
#
# root.attributes("-alpha", 0.95)
# root.attributes("-toolwindow", True)
#
# root.mainloop()