
import pandas as pd  # For data manipulation tasks on Excel files
import os
import numpy as np  # (Optional) For numerical computations
import seaborn as sns
import matplotlib.pyplot as plt


# Volume A: Covers flank openings and irregular starts, such as 1.b4 (Polish Opening) or 1.g3 (King’s Fianchetto). These are openings that don’t fit into the more structured categories of the other volumes.
#
# Volume B: Focuses on openings where White plays 1.e4 and Black responds with moves other than 1...e5 or 1...e6. This includes the Sicilian Defense (1.e4 c5) and other responses like the French Defense (1.e4 e6).
# Volume C: Includes double King pawn openings, where both players start with 1.e4 e5. This volume covers openings like the Ruy Lopez, Italian Game, and Petroff Defense.
#
# Volume D: Deals with double Queen pawn openings, where White plays 1.d4 and Black responds with 1...d5. This includes the Queen’s Gambit, Slav Defense, and other 1.d4 structures.
#
# Volume E: Covers openings where Black responds to 1.d4 with moves like 1...Nf6 followed by 2...e6 or 2...g6. This includes the King’s Indian Defense, Grünfeld Defense, and other hypermodern openings.

df = pd.read_csv(r"C:\Users\laith\Downloads\semumods\updated_with_opening_group.csv")


print(df.head())

gd= df.groupby(['opening_group','winner']).size().reset_index(name='counts')
print(gd.head())
gd['y_axis_label'] = gd['opening_group'] + " - " + gd['winner']

gd = gd.sort_values(by='counts', ascending=True)

# Extract data for the plot
y_labels = gd['y_axis_label']  # Combined labels for the y-axis
x_values = gd['counts']  # Counts for the x-axis


plt.figure(figsize=(10, 8))
plt.barh(y_labels, x_values, color='skyblue', edgecolor='black')

# Customize the plot
plt.title('Comparison Between Winner Color and Opening Group', fontsize=14)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Opening Group and Winner Color', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()




#df['opening_group'] = df['opening_eco'].apply(lambda x: str(x)[0] if pd.notnull(x) and len(str(x)) > 0 else None)
# def extract_first_5_moves(moves):
#     move_list = str(moves).split()  # Split moves into a list (ensure moves is a string)
#     first_10_half_moves = move_list[:10]  # Get the first 10 half-moves
#     return " ".join(first_10_half_moves)  # Join them back into a single string
# df= df.drop(columns=['game_id','white_id','black_id'])

# color_counts = df["winner"].value_counts()

# # Plot the counts in stacked format
# color_counts.plot(
#     kind="bar",
#     stacked=True,
#     color=['red', 'blue', 'green'],
#     figsize=(8, 5)
# )
#
# # Add labels and title
# plt.title("Stacked Bar Chart: Winning Colors Counts")
# plt.xlabel("Winner (Color)")
# plt.ylabel("Count of Wins")
# plt.xticks(rotation=0)  # Keeps x-axis readable
# plt.tight_layout()
# plt.show()



# Step 3: Apply the function to the 'Moves' column and create a new column
# df["First_5_Moves"] = df["moves"].apply(extract_first_5_moves)
# df.to_excel("updated_file.xlsx", index=False)
# file_path = os.path.abspath("updated_file.xlsx")
# print(f"The updated file is saved at: {file_path}")

# df['move_list']=df['First_5_Moves'].str.split()
# df["FirstWhiteMove"] = df["move_list"].apply(lambda x: x[0] if len(x) > 0 else None)
# df["FirstBlackMove"]=df["move_list"].apply(lambda x: x[1] if len(x)>1 else None)
#
# white_moves=df['FirstWhiteMove'].value_counts().head(5)
# black_moves=df['FirstBlackMove'].value_counts().head(5)







