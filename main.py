import random
import pandas as pd
from math import ceil

# Data mahasiswa
data = [
    ("2404140001","YUN SABARINA MIKANDA","F"),
    ("2404140002","TANAYA FADHIL DANISWARA","M"),
    ("2404140003","MECCA ROBBANI ARIANTO","M"),
    ("2404140004","ALINA FADLILA SYIFA","F"),
    ("2404140005","Ananda Khairu Amalinaa","F"),
    ("2404140006","SAMUEL ADITYAS GUNAWAN FITRIANTO","M"),
    ("2404140007","Dian Pranawan Ningtyas","F"),
    ("2404140008","Aditya Arga Kusuma","M"),
    ("2404140009","SAVA ADIWIDYA MAULANA","M"),
    ("2404140010","DIMAS SUGIARTO","M"),
    ("2404140011","Muhammad Raja Fahada","M"),
    ("2404140014","Muhammad Khalid Misy'al","M"),
    ("2404140018","Eugenie Friskyla","F"),
    ("2404140021","BAGAS SATRIO HIMAWAN","M"),
    ("2404140022","Adhitya Raynar Indrasta","M"),
    ("2404140024","NADA NAFISAH","F"),
    ("2404140025","ITSNAN NUR KHANIFAH","F"),
    ("2404140026","ARVIAN POETRA SADEWA","M"),
    ("2404140027","NURAINI PUTRI CAHYANINGRUM","F"),
    ("2404140028","ASYAM NUR ASSHIDDIQ","M"),
    ("2404140029","ANNISA YUSRI NUR ROCHMAH","F"),
    ("2404140030","PUTRI RASYIDAH DINANTI","F"),
    ("2404140041","Muhammad Ikhsanul Fikri Ramadhan","M"),
    ("2404140042","Alya Fuji Insani","F"),
    ("2404140043","Fathimah Shaffa' Abqariyya","F"),
    ("2404140044","Yakobus Dimas Setiawan","M"),
    ("2404140045","AKHMAD DANIL","M"),
    ("2404140046","BAGAS PERMANA PUTRA","M"),
    ("2404140047","Afza Muhammad Chattab El-Faiz","M"),
    ("2404140048","MUHAMAD NUR IMAN","M"),
    ("2404140049","RADITYA ATMA AZIZ","M"),
    ("2404140050","ERLANG AQILA DINAR DEWANGGA","M"),
    ("2404140061","GILANG MUHARAM","M"),
    ("2404140062","NABIL FADHILAH ALFARIZKY","M"),
    ("2404140063","MAHENDRA ARQUDANTA","M"),
    ("2404140064","NAZZWA VIENTIKA TRIANA","F"),
    ("2404140065","NATASYA AULIA","F"),
    ("2404140066","WASIDAH LAILATUS SABIQOH","F"),
    ("2404140067","SHOFI ALISHA","F"),
    ("2404140068","YESSY SHAFITRI","F"),
    ("2404140069","TOMI ADYATMA","M"),
    ("2404140070","MUHAMMAD RYAN RAMADHAN","M"),
    ("2404140074","ARIEL JAMES MALORINGAN","M"),
    ("2404140081","NAUFAL RIZQI FERDIANSYAH","M"),
    ("2404140082","TAN MAULA TSAQIF IBRAHIM","M"),
    ("2404140083","ADEBAYU NIZAR AZZAMY","M"),
    ("2404140084","RISTA AZ-ZAHRA NOVITA WIJAYA","F"),
    ("2404140085","HERDI RIZKY GUNAWAN","M"),
    ("2404140086","FAWAZ ZAYANA ATHA RASENDRIYA","M"),
    ("2404140087","RADHITYA MAHESWARA ARYAPRATAMA","M"),
    ("2404140088","ZENZAENA ATAME RISSAN","F"),
    ("2404140089","RAFI PUTRA RINDJANI HOEFNAGEL","M"),
    ("2404140090","IRFAN FATKHURRIZAL","M"),
]

TOTAL_MAHASISWA = len(data)

def get_user_input(prompt, type=str, options=None):
    """Fungsi untuk mengambil input pengguna dengan validasi sederhana."""
    while True:
        try:
            print(f"|  > {prompt}", end=" ")
            user_input = input()
            if type == int:
                val = int(user_input)
                return val
            elif type == str:
                if options and user_input.upper() not in options:
                    print("|  [!] Pilihan tidak valid. Harap masukkan salah satu:", ', '.join(options))
                    continue
                return user_input.strip()
        except ValueError:
            print("|  [!] Input harus berupa angka.")
        except EOFError:
            # Handle Ctrl+D or end of file
            print("\n|  [!] Input dibatalkan.")
            exit()
            
def display_header(title):
    """Fungsi untuk mencetak header CLI yang mirip 'yarn'."""
    print("\n" + "="*50)
    print(f"| {title.upper()}")
    print("="*50)

def display_status(label, value):
    """Fungsi untuk mencetak status konfigurasi."""
    print(f"| ✅ {label}: {value}")

# --- Bagian Konfigurasi ---
def get_group_config():
    """Mengambil konfigurasi kelompok dari pengguna."""
    display_header("⚙️ KONFIGURASI PEMBAGIAN KELOMPOK")
    display_status("Total Mahasiswa", TOTAL_MAHASISWA)

    # 1. Tentukan jumlah kelompok
    while True:
        N_GROUPS = get_user_input("Jumlah kelompok yang diinginkan:", int)
        if N_GROUPS <= 0:
            print("|  [!] Jumlah kelompok minimal 1.")
        elif N_GROUPS > TOTAL_MAHASISWA:
            print(f"|  [!] Jumlah kelompok ({N_GROUPS}) tidak boleh melebihi total mahasiswa ({TOTAL_MAHASISWA}).")
        else:
            break
    display_status("Jumlah Kelompok", N_GROUPS)

    # 2. Tentukan ukuran kelompok
    while True:
        GROUP_SIZE = get_user_input("Ukuran anggota per kelompok (misal: 4-5 atau 5):", str)
        GROUP_SIZES = []
        try:
            if '-' in GROUP_SIZE:
                min_size, max_size = map(int, GROUP_SIZE.split('-'))
                if min_size <= 0 or max_size <= 0: raise ValueError
            else:
                min_size = max_size = int(GROUP_SIZE)
                if min_size <= 0: raise ValueError

            base_size = TOTAL_MAHASISWA // N_GROUPS
            remainder = TOTAL_MAHASISWA % N_GROUPS
            
            GROUP_SIZES = [base_size + 1] * remainder + [base_size] * (N_GROUPS - remainder)
            
            if min(GROUP_SIZES) < min_size or max(GROUP_SIZES) > max_size:
                 print(f"|  [!] Ukuran kelompok yang dihasilkan ({min(GROUP_SIZES)}-{max(GROUP_SIZES)}) tidak sesuai dengan rentang yang diminta ({min_size}-{max_size}).")
                 continue
            if max_size * N_GROUPS < TOTAL_MAHASISWA:
                print(f"|  [!] Total maksimum anggota ({max_size * N_GROUPS}) kurang dari total mahasiswa ({TOTAL_MAHASISWA}). Perlu ukuran kelompok yang lebih besar.")
                continue

            print(f"|  > Ukuran kelompok yang akan digunakan: {GROUP_SIZES}")
            break
        except ValueError:
            print("|  [!] Format ukuran tidak valid. Gunakan format 'N' atau 'Min-Max'.")
    display_status("Ukuran Kelompok", f"{GROUP_SIZES[0]}-{GROUP_SIZES[-1]} (Total {TOTAL_MAHASISWA} orang)")

    # 3. Tentukan ketua
    LEADERS = []
    
    IS_RANDOM_LEADER = get_user_input("Ketua kelompok ditentukan acak? (Y/N):", str, options=["Y", "N"]).upper() == "Y"
    display_status("Ketua Acak", IS_RANDOM_LEADER)

    if IS_RANDOM_LEADER:
        all_names = [d[1] for d in data]
        if N_GROUPS > TOTAL_MAHASISWA: N_GROUPS = TOTAL_MAHASISWA
        LEADERS = random.sample(all_names, N_GROUPS)
    else:
        display_header("👥 PILIH KETUA KELOMPOK")
        all_names = [d[1] for d in data]
        
        print("| Daftar Mahasiswa:")
        for i, name in enumerate(all_names):
            print(f"| {i+1:02d}. {name}")

        for i in range(N_GROUPS):
            while True:
                leader_index = get_user_input(f"Pilih ketua ke-{i+1} (No.):", int)
                if 1 <= leader_index <= len(all_names):
                    leader_name = all_names[leader_index - 1]
                    if leader_name not in LEADERS:
                        LEADERS.append(leader_name)
                        print(f"|    -> Ketua {i+1}: {leader_name}")
                        break
                    else:
                        print("|  [!] Nama ini sudah dipilih sebagai ketua.")
                else:
                    print("|  [!] Nomor tidak valid.")

    return LEADERS, GROUP_SIZES

# --- Bagian Logika Pembagian Kelompok ---
def assign_groups(data, leaders, group_sizes):
    """Melakukan pembagian kelompok dengan syarat minimal 1 perempuan per kelompok."""
    
    # 1. Inisialisasi kelompok dan masukkan ketua
    groups = {i+1: [] for i in range(len(leaders))}
    leader_data_map = {d[1].lower(): (d[0], d[1], d[2]) for d in data}
    
    for i, leader in enumerate(leaders, start=1):
        d = leader_data_map.get(leader.lower())
        if d:
            groups[i].append((d[0], d[1], d[2], "Yes"))

    # Pisahkan anggota lain
    remaining = [d for d in data if d[1] not in leaders]
    
    # 2. Pisahkan anggota yang tersisa berdasarkan Gender
    remaining_females = [d for d in remaining if d[2] == "F"]
    remaining_males = [d for d in remaining if d[2] == "M"]

    random.shuffle(remaining_females)
    random.shuffle(remaining_males)

    # 3. Alokasikan satu perempuan ke setiap kelompok yang belum memiliki perempuan
    for i in range(len(leaders)):
        group_id = i + 1
        current_size = len(groups[group_id])
        
        if current_size >= group_sizes[i]: # Lewati jika sudah penuh
            continue

        has_female = any(member[2] == "F" for member in groups[group_id])
        if not has_female and remaining_females:
            person = remaining_females.pop(0)
            groups[group_id].append((person[0], person[1], person[2], "No"))

    # 4. Gabungkan sisa dan alokasikan secara acak untuk mengisi kuota
    remaining_all = remaining_females + remaining_males
    random.shuffle(remaining_all)

    for i in range(len(leaders)):
        group_id = i + 1
        group_limit = group_sizes[i]
        
        while len(groups[group_id]) < group_limit and remaining_all:
            person = remaining_all.pop()
            groups[group_id].append((person[0], person[1], person[2], "No"))
            
    return groups

# --- Bagian Output ---
def print_result(groups):
    """Mencetak hasil pembagian kelompok dalam format tabel yang jelas."""
    display_header("📋 HASIL PEMBAGIAN KELOMPOK")
    for gnum, members in groups.items():
        # Sort members within the group to place the leader first
        members.sort(key=lambda x: x[3], reverse=True)
        
        # Get the leader's name for the header
        leader_name = next((m[1] for m in members if m[3] == "Yes"), "TIDAK ADA KETUA")
        
        print("-" * 50)
        print(f"| KELOMPOK {gnum} (Total Anggota: {len(members)}) | Ketua: {leader_name}")
        print("-" * 50)
        
        # Create a temporary DataFrame for the current group
        rows = []
        for i, m in enumerate(members):
            rows.append((i+1, m[0], m[1], m[2], m[3]))
            
        df_group = pd.DataFrame(rows, columns=["No.", "NIM", "Nama", "Gender", "Ketua"])
        
        # Print the DataFrame without the index
        print(df_group.to_string(index=False))

# --- Main Program ---
if __name__ == "__main__":
    try:
        leaders, group_sizes = get_group_config()
        
        # Cek apakah jumlah ketua sesuai dengan jumlah kelompok yang diminta
        if len(leaders) != len(group_sizes):
            print("\n| [!!!] Jumlah ketua tidak sesuai dengan jumlah kelompok yang dihitung. Silakan ulangi konfigurasi.")
        else:
            final_groups = assign_groups(data, leaders, group_sizes)
            print_result(final_groups)
    except KeyboardInterrupt:
        print("\n|  [!] Program dibatalkan oleh pengguna.")
    except Exception as e:
        print(f"\n| [!!!] Terjadi kesalahan: {e}")
        print("| Pastikan input Anda benar dan jumlah kelompok/anggota sesuai dengan total mahasiswa.")