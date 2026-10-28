\# Event Registration API



REST API untuk mengelola acara kampus, peserta, dan pendaftaran acara. Proyek ini dibuat menggunakan Python dan FastAPI sebagai tugas Pemrograman Lanjutan.



\## Fitur



\- Membuat dan melihat daftar event.

\- Mendaftarkan peserta dan melihat daftar peserta.

\- Mendaftarkan peserta ke event.

\- Menolak pendaftaran ganda pada event yang sama.

\- Menolak pendaftaran jika kuota event sudah penuh.

\- Validasi data menggunakan Pydantic.

\- Unit testing menggunakan Pytest.



\## Teknologi



\- Python 3.11

\- FastAPI

\- Uvicorn

\- Pydantic

\- Pytest

\- Git



\## Struktur Proyek



```text

event-registration-api/

├── app/

│   ├── api/

│   │   ├── event\_routes.py

│   │   ├── participant\_routes.py

│   │   └── registration\_routes.py

│   ├── models/

│   ├── repositories/

│   ├── services/

│   ├── dependencies.py

│   └── main.py

├── tests/

│   └── test\_registration\_service.py

├── .gitignore

├── requirements.txt

└── README.md

```



\## Instalasi



Pastikan Python 3.11 atau versi kompatibel sudah terpasang.



1\. Aktifkan virtual environment.

2\. Instal dependensi:



```bash

python -m pip install -r requirements.txt

```



\## Menjalankan API



Jalankan perintah:



```bash

python -m uvicorn app.main:app --reload

```



Buka dokumentasi interaktif API di:



http://127.0.0.1:8000/docs



Endpoint pemeriksaan kesehatan:



http://127.0.0.1:8000/health



\## Endpoint API



| Method | Endpoint | Fungsi |

|---|---|---|

| GET | `/` | Pesan sambutan |

| GET | `/health` | Pemeriksaan status API |

| POST | `/events/` | Membuat event |

| GET | `/events/` | Melihat semua event |

| POST | `/participants/` | Membuat peserta |

| GET | `/participants/` | Melihat semua peserta |

| POST | `/registrations/` | Mendaftarkan peserta ke event |

| GET | `/registrations/` | Melihat semua pendaftaran |



\## Menjalankan Unit Test



Jalankan:



```bash

python -m pytest -v

```



Test mencakup pendaftaran berhasil, penolakan pendaftaran ganda, dan penolakan pendaftaran ketika kuota penuh.



\## Arsitektur



\- \*\*Models:\*\* mendefinisikan struktur dan validasi data.

\- \*\*Repositories:\*\* mengelola penyimpanan serta pengambilan data.

\- \*\*Services:\*\* menerapkan aturan bisnis.

\- \*\*API Routes:\*\* menerima request dan mengembalikan response.

\- \*\*Dependencies:\*\* menyediakan repository bersama kepada route.



Pemisahan tersebut membantu menjaga kode tetap modular dan lebih mudah diuji.



\## Catatan



Saat ini data disimpan di memori (\*in-memory\*). Data akan kembali kosong ketika aplikasi dimulai ulang. Penyimpanan permanen menggunakan SQLite belum diterapkan.



\## Status Proyek



Versi awal API telah dibuat dan tiga unit test utama berhasil dijalankan.



