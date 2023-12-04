drop table if exists services;
create table services (
	id serial,
	nama_montir text,
	nama_motor text,
	transmisi text,
	yang_ditangani text,
	harga_servis text,
	servis_ke text,
	waktu_pengerjaan text,
	tanggal_pengerjaan date
);

insert into services (nama_montir, nama_motor, transmisi, yang_ditangani, harga_servis, servis_ke, waktu_pengerjaan, tanggal_pengerjaan) 
values
	('Andi', 'BeAT Sporty CBS ISS SPION PLUS', 'Matic', '["Perawatan", "Ganti Ban"]', 250000, 1, '32 Menit', '2023-11-26'),
	('Karyono', 'NF11C1C M/T', 'Cub', '["Perawatan", "Ganti Oli"]', 200000, 5, '46 Menit', '2023-10-26'),
	('Karyono', 'NEW SUPRA CW FI', 'Cub', '["Ganti Aki"]', 200000, 2, '25 Menit', '2023-11-26'),
	('Andi', 'VARIO 125 CBS JKT SF DL', 'Matic', '["Perawatan"]', 100000, 3, '20 Menit', '2023-11-26'),
	('Subagja', 'NEW SUPRA CW FI', 'Cub', '["Ganti Oli"]', 125000, 4, '25 Menit', '2023-11-26'),
	('Karyono', 'NF125TR3 M/T', 'Cub', '["Perawatan", "Ganti Oli", "Ganti Ban", "Ganti Aki"]', 450000, 6, '60 Menit', '2023-11-26'),
	('Andi', 'NEW VARIO TECHNO PGM FI', 'Matic', '["Perawatan"]', 100000, 1, '27 Menit', '2022-10-07'),
	('Subagja', 'ALL NEW VARIO 125 FI CBS', 'Matic', '["Ganti Oli", "Ganti Ban", "Ganti Aki"]', 350000, 2, '52 Menit', '2023-11-26'),
	('Andi', 'NEW REVO FIT MC', 'Cub', '["Perawatan"]', 100000, 3, '25 Menit', '2022-10-09'),
	('Karyono', 'NEW BEAT ESP CBS PLUS', 'Matic', '["Perawatan"]', 100000, 4, '26 Menit', '2022-10-11')
	;