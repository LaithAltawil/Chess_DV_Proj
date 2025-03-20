
import pandas as pd  # For data manipulation tasks on Excel files
import os
import numpy as np  # (Optional) For numerical computations
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\laith\PycharmProjects\PythonProject3\updated_file.xlsx")

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

df['move_list']=df['First_5_Moves'].str.split()
df["FirstWhiteMove"] = df["move_list"].apply(lambda x: x[0] if len(x) > 0 else None)
df["FirstBlackMove"]=df["move_list"].apply(lambda x: x[1] if len(x)>1 else None)

white_moves=df['FirstWhiteMove'].value_counts().head(5)
black_moves=df['FirstBlackMove'].value_counts().head(5)







