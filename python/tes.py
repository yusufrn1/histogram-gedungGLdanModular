import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data
df = pd.read_excel("wifi.xlsx")

# Filter hanya responden yang pilih satu lokasi (bukan 'Keduanya')
df_filtered = df[df["1. Di gedung mana kamu biasa menggunakan Wi-Fi kampus?"].isin(["Gedung Griya Legita", "Gedung Modular"])]

# Pisahkan per lokasi
griya = df_filtered[df_filtered["1. Di gedung mana kamu biasa menggunakan Wi-Fi kampus?"] == "Gedung Griya Legita"]["3. Berapa tingkat kepuasan anda terhadap koneksi Wi-Fi di lokasi tersebut? (Skala 1–10)"]
modular = df_filtered[df_filtered["1. Di gedung mana kamu biasa menggunakan Wi-Fi kampus?"] == "Gedung Modular"]["3. Berapa tingkat kepuasan anda terhadap koneksi Wi-Fi di lokasi tersebut? (Skala 1–10)"]

# Buat histogram berdampingan
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
sns.histplot(griya, bins=range(1,12), kde=False, color="skyblue")
plt.title("Distribusi Kepuasan - Griya Legita")
plt.xlabel("Skor Kepuasan")
plt.ylabel("Frekuensi")

plt.subplot(1,2,2)
sns.histplot(modular, bins=range(1,12), kde=False, color="salmon")
plt.title("Distribusi Kepuasan - Modular")
plt.xlabel("Skor Kepuasan")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()
