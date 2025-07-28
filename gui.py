import ttkbootstrap as ttk
from tkinter import StringVar, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from calculator import calculate_roi


def create_gui():
    app = ttk.Window("Real Estate ROI Calculator with Chart", themename="minty",
                     size=(1300, 920))  # Set window size to 1200x700

    # Title
    ttk.Label(app, text="🏡 Real Estate ROI Calculator (China)", font=("Times New Roman", 24, "bold")).grid(row=0,
                                                                                                            columnspan=2,
                                                                                                            pady=5,
                                                                                                            sticky="n")

    # Input Frame (Upper left)
    frame_input = ttk.Frame(app, padding=20, width=150)
    frame_input.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")  # Left side for input fields
    # Make inputs responsive
    app.grid_columnconfigure(0, weight=2)

    # Summary Frame (Upper right)
    frame_summary = ttk.Frame(app, padding=20, width=200)
    frame_summary.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")  # Right side for summary text
    app.grid_columnconfigure(1, weight=2)

    # Input Heading
    ttk.Label(frame_input, text="Inputs", font=("Times New Roman", 18, "bold")).grid(row=0, columnspan=2, pady=5,
                                                                                     sticky="w")

    # Input Widgets (placed on upper-left)
    ttk.Label(frame_input, text="🏠 Property Price (Wan):", font=("Times New Roman", 14)).grid(row=1, column=0,
                                                                                               sticky="e", pady=5)
    entry_price = ttk.Entry(frame_input, width=20, font=("Times New Roman", 14))
    entry_price.grid(row=1, column=1)

    ttk.Label(frame_input, text="💰 Monthly Rent (RMB):", font=("Times New Roman", 14)).grid(row=2, column=0,
                                                                                             sticky="e", pady=5)
    entry_rent = ttk.Entry(frame_input, width=20, font=("Times New Roman", 14))
    entry_rent.grid(row=2, column=1)

    ttk.Label(frame_input, text="📉 Occupancy Rate (%):", font=("Times New Roman", 14)).grid(row=3, column=0,
                                                                                             sticky="e", pady=5)
    entry_occupancy = ttk.Entry(frame_input, width=20, font=("Times New Roman", 14))
    entry_occupancy.grid(row=3, column=1)

    ttk.Label(frame_input, text="📊 Interest Rate (%):", font=("Times New Roman", 14)).grid(row=4, column=0, sticky="e",
                                                                                            pady=5)
    entry_interest = ttk.Entry(frame_input, width=20, font=("Times New Roman", 14))
    entry_interest.grid(row=4, column=1)

    ttk.Label(frame_input, text="📆 Loan Duration (Years):", font=("Times New Roman", 14)).grid(row=5, column=0,
                                                                                                sticky="e", pady=5)
    entry_years = ttk.Entry(frame_input, width=20, font=("Times New Roman", 14))
    entry_years.grid(row=5, column=1)

    # Define a custom style for the button (completely round and Times New Roman font)
    style = ttk.Style()
    style.configure("TButton",
                    font=("Times New Roman", 14, "bold"),
                    padding=(20, 10),  # Adjust padding for button size
                    relief="flat",  # Remove 3D effect
                    borderwidth=0,  # Remove border
                    background="#4CAF50",  # Button background color
                    foreground="white",  # Text color
                    highlightthickness=0,  # Removing highlight border
                    anchor="center",  # Ensure text is centered in button
                    width=20,  # Ensures the button has a consistent width
                    height=2)  # Set height to make sure it expands vertically

    # Add hover effect to button (change color when hovered over)
    style.map("TButton",
              background=[('active', '#45a049'), ('!active', '#4CAF50')])  # Color change on hover

    # Create the round button with style
    ttk.Button(frame_input, text="📌 Calculate & Plot ROI", style="TButton",
               command=lambda: calculate_and_plot(entry_price, entry_rent, entry_occupancy, entry_interest,
                                                  entry_years, summary_text, canvas, ax)).grid(row=6, columnspan=2,
                                                                                               pady=20, sticky="ew")

    # Summary Heading (Using grid layout and matching Input Heading style)
    ttk.Label(frame_summary, text="Summary", font=("Times New Roman", 18, "bold")).grid(row=0, columnspan=2, pady=5,
                                                                                        sticky="w")
    # Summary Text
    summary_text = ttk.Label(frame_summary, text="Summary will appear here...", font=("Times New Roman", 14),
                             justify="left")
    summary_text.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

    # Graph Heading
    ttk.Label(app, text="Graph", font=("Times New Roman", 18, "bold")).grid(row=2, columnspan=2, pady=5, sticky="w")

    # Matplotlib Figure (Below input and summary)
    fig, ax = plt.subplots(figsize=(12, 7), dpi=110)  # Adjusted figure size for the plot
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5,
                                sticky="nsew")  # Bottom section for the graph
    canvas.draw()

    # Configure grid weight to make the layout responsive
    app.grid_rowconfigure(0, weight=0)  # Row for title (non-resizable)
    app.grid_rowconfigure(1, weight=1)  # Row for inputs and summary (resizable)
    app.grid_rowconfigure(2, weight=0)  # Row for graph heading (non-resizable)
    app.grid_rowconfigure(3, weight=3)  # Row for the graph (resizable)

    app.grid_columnconfigure(0, weight=1)  # Left column (input fields)
    app.grid_columnconfigure(1, weight=1)  # Right column (summary text)

    # Stop the program when the window is closed
    app.protocol("WM_DELETE_WINDOW", app.quit)

    return app, entry_price, entry_rent, entry_occupancy, entry_interest, entry_years, summary_text, canvas, ax


def calculate_and_plot(entry_price, entry_rent, entry_occupancy, entry_interest, entry_years, summary_text, canvas, ax):
    try:
        # Get values from the inputs
        price = float(entry_price.get())
        rent_monthly = float(entry_rent.get())
        occupancy = float(entry_occupancy.get()) / 100
        interest_rate = float(entry_interest.get()) / 100
        loan_years = int(entry_years.get())

        # Call the calculation function from calculator.py
        annual_cashflow, cumulative_equity, remaining_balance, rent_annual, monthly_payment = calculate_roi(price,
                                                                                                            rent_monthly,
                                                                                                            occupancy,
                                                                                                            interest_rate,
                                                                                                            loan_years)

        # Clear and plot new figure
        ax.clear()
        ax.plot(range(1, loan_years + 1), annual_cashflow, label="Annual Cash Flow")
        ax.plot(range(1, loan_years + 1), cumulative_equity, label="Cumulative Equity")
        ax.plot(range(1, loan_years + 1), remaining_balance, label="Remaining Loan Balance")
        ax.set_title("📊 30-Year Investment Projection", fontsize=14)
        ax.set_xlabel("Year")
        ax.set_ylabel("Amount (RMB)")
        ax.legend()
        canvas.draw()

        # Update summary text
        gross_yield = (rent_annual / price) * 100
        net_cash_flow = annual_cashflow[0]

        summary_text.config(
            text=(
                f"🏠 Property Price: ¥{price:,.0f}\n"
                f"📈 Effective Annual Rent: ¥{rent_annual:,.0f}\n"
                f"📉 Year-1 Mortgage Payment: ¥{monthly_payment * 12:,.0f}\n"
                f"💸 Year-1 Net Annual Cash Flow: ¥{net_cash_flow:,.0f}\n"
                f"📊 Gross Rental Yield: {gross_yield:.2f}%"
            )
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric inputs.")
