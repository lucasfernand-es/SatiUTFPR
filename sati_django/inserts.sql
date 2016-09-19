Insert INTO sati_edition(id, name, begin_date, end_date, theme, description, is_active)
values (1, 'Sati 2016', 'September 26, 2016', 'September 30, 2016', 'Acessibilidade', 'Evento do departamento de informática da UTFPR de Ponta Grossa', TRUE );

INSERT INTO sati_category(id, name, image) VALUES
  (1, 'Minicurso', 'minicurso.jpg'),
  (2, 'Oficina', 'oficina.jpg'),
  (3, 'Palestra', 'palestra.jpg'),
  (4, 'WPCCG', 'wpccg.png'),
  (5, 'Outro', 'outro.jpg');

INSERT INTO sati_event(id, name, fee, workload, description, is_active, category_id, edition_id) VALUES
  (1, 'Minicurso Latex', 10, 0, ' Minicurso latex article(Segunda) e (Beamer)', true, 1, 1),
  (2, 'Programando Robôs Cognitivos Usando o ARGO', 10, 16, 'Programando Robôs Cognitivos Usando o ARGO', true, 2, 1),
  (3, 'Abertura Oficial', 0, 0, 'Cerimönia de abertura da Sati.', true, 5, 1),
  (4, 'Regulamentação da Profissão', 0, 0, 'Palestra sobre as vantagens e desvantagens da regulamentação da profissão.', true, 3, 1),
  (5, 'Desenvolvimento de aplicações em realidades aumentada e virtual', 0, 0, 'Palestra sobre realidade aumentada e virtual', true, 3, 1),
  (6, 'Internet das coisas: tecnologia inteligente', 0, 0, 'Palestra sobre internet das coisas', true, 3, 1),
  (7, 'Balence em jogos', 10, 0, 'Oficina sobre balence.', true, 2, 1),
  (8, 'Utilizando Sistemas Multi-Agentes para Programação de Plataformas Robóticas', 0, 0, 'Utilizando Sistemas Multi-Agentes para Programação de Plataformas Robóticas', true, 3, 1),
  (9, 'Interação humano computador com ênfase em acessibilidade', 0, 0, 'Interação humano computador com ênfase em acessibilidade', true, 2, 1),
  (10, 'WPCCG', 0, 0, 'Workshop', true, 4, 1),
  (11, 'Campeonato de e-sports', 0, 0, 'Campeonato de e-sports: FIFA (Quarta-Feira) E CS:GO(Quinta-Feira)', true, 5, 1),
  (12, 'Internacionalização das Empresas de TI', 0,0, 'Palestra sobre Internacionalização das Empresas de TI', true, 3, 1),
  (13, 'Tema: Global Game Jam e jogos em geral', 0, 0, 'Palestra: Global Game Jam e jogos em geral', true, 3, 1),
  (14, 'Canvas', 0, 0, 'Oficina sobre canvas', true, 2, 1),
  (15, 'Drones na área acadêmica, aplicação real e desmitificação', 0, 0, 'Drones na área acadêmica, aplicação real e desmitificação', true, 3, 1),
  (16, 'Unreal', 10, 0, 'Minicurso sobre a engine unreal.', true, 1, 1),
  (17, 'Photoshop', 10, 0, 'Minicurso photoshop', true, 1, 1),
  (18, 'Dispositivos alternativos de interação.', 0, 0, 'Dispositivos alternativos de interação.', true, 2, 1),
  (19, 'Marco Civil da Internet.', 0, 0, 'Marco Civil da Internet.', true, 3, 1),
  (20, 'Desenvolvimento de jogos em HTML 5.', 10, 0, 'Desenvolvimento de jogos em HTML 5', true, 1, 1),
  (21, 'Palestra IPv6', 10, 0, 'Palestra sobre IPv6', true, 3, 1 ),
  (22, 'Maratona de Programação', 0, 0, 'Maratona de Programação', true, 5, 1);

INSERT INTO SATI_PERSON (id, name, password, institution, cpf, academic_registry, email, is_active, role)
values
  (1, 'Aleffer Rocha', 'senha', 'UTFPR', 111111, 11111 ,'1@email.com', true, 1),
  (2, 'Professor Carlos Pantoja', 'senha', 'UTFPR', 22222, 11111 ,'2@email.com', true, 1),
  (3, 'Marcio Funes', 'senha', 'UTFPR', 33333, 11111 ,'3@email.com', true, 1),
  (4, 'Diversos', 'senha', 'UTFPR', 4444, 11111 ,'4@email.com', true, 1),
  (5, 'Roberto S. Bigonha', 'senha', 'UTFPR', 66666, 11111 ,'6@email.com', true, 1),
  (6, 'Thiago Moura', 'senha', 'UTFPR', 66866, 11111 ,'16@email.com', true, 1),
  (7, 'Leonardo', 'senha', 'UTFPR', 661116, 11111 ,'8@email.com', true, 1),
  (8, 'Filipe Franchini', 'senha', 'UTFPR', 63666, 11111 ,'123@email.com', true, 1),
  (9, 'Robert Janssen', 'senha', 'UTFPR', 123566, 11111 ,'123333@email.com', true, 1),
  (10, 'Bruno Campagnolo', 'senha', 'UTFPR', 1223166, 11111 ,'1112333@email.com', true, 1),
  (11, 'Ronald Wolochn', 'senha', 'UTFPR', 12231888, 11111 ,'188333@email.com', true, 1),
  (12, 'Malcon', 'senha', 'UTFPR', 122318848, 11111 ,'1883323@email.com', true, 1),
  (13, 'Rafael Althaus', 'senha', 'UTFPR', 12324441888, 11111 ,'18844333@email.com', true, 1),
  (14, 'Rafael Althaus', 'senha', 'UTFPR', 122164441888, 11111 ,'1884444333@email.com', true, 1),
  (15, 'Sandro Alex', 'senha', 'UTFPR', 1224414145888, 11111 ,'18855544333@email.com', true, 1),
  (16, 'Luciano Santos', 'senha', 'UTFPR', 222234521, 111111, 'bbbe3334@email.com', true, 1),
  (17, 'Saulo/Alessandro', 'senha', 'UTFPR', 24666664, 212356, '345234@email.com', true, 1);

-- INSERT INTO AUTH_USER(password, username, is_staff, is_active, email, first_name, last_name,is_superuser, date_joined)
-- VALUES
-- ('teste', 'nome', true, true, 'email', 'first', 'last', false, now())

INSERT INTO sati_session(id, spots, is_active, event_id, instructor_id) VALUES
  (1, 10, true, 1, 1),
  (2, 10, true, 2, 2),
  (3, 10, true, 3, 4),
  (4, 10, true, 4, 5),
  (5, 10, true, 5, 3),
  (6, 10, true, 6, 6),
  (7, 10, true, 7, 7),
  (8, 10, true, 8, 2),
  (9, 10, true, 9, 3),
  (10, 10, true, 10, 4),
  (11, 10, true, 11, 4),
  (12, 10, true, 12, 9),
  (13, 10, true, 13, 10),
  (14, 10, true, 14, 11),
  (15, 10, true, 15, 12),
  (16, 10, true, 16, 13),
  (17, 10, true, 17, 8),
  (18, 10, true, 18, 10),
  (19, 10, true, 19, 15),
  (20, 10, true, 20, 3),
  (21, 10, true, 11, 4),
  (22, 10, true, 21, 16),
  (23, 10, true, 22, 17),
  (24, 10, true, 1, 1);



INSERT INTO sati_room(id, name, occupancy, number, type, is_active) VALUES
  (1, 'Laboratório V', 30, 203, 'Laboratório', true),
  (2, 'Laboratório VII', 30, 203, 'Laboratório', true),
  (3, 'Laboratório II', 30, 203, 'Laboratório', true),
  (4, 'Laboratório I', 30, 203, 'Laboratório', true),
  (5, 'Auditório', 100, 100, 'Auditorio', true),
  (6, 'Mini Auditório', 100, 102, 'Auditorio', true),
  (7, 'Laboratório VI', 30, 203, 'Laboratório', true),
  (8, 'Laboratório III', 30, 203, 'Laboratório', true);




INSERT INTO sati_occurrence(id, begin_date_time, end_date_time, is_active, room_id, session_id) VALUES
  -- Dia 26
  (1, 'September 26 08:20:00 2016', 'September 26 12:00:00 2016', true, 1, 1),
  (2, 'September 26 08:20:00 2016', 'September 26 12:00:00 2016', true, 2, 2),
  (3, 'September 26 10:20:00 2016', 'September 26 12:00:00 2016', true, 4, 20),
  (4, 'September 26 13:50:00 2016', 'September 26 17:30:00 2016', true, 2, 2),
  (5, 'September 26 18:40:00 2016', 'September 26 19:30:00 2016', true, 5, 3),
  (6, 'September 26 19:30:00 2016', 'September 26 20:20:00 2016', true, 5, 4),
  -- Dia 27
  (7, 'September 27 08:20:00 2016', 'September 27 12:00:00 2016', true, 2, 2),
  (8, 'September 27 10:20:00 2016', 'September 27 12:00:00 2016', true, 5, 5),
  (9, 'September 27 12:00:00 2016', 'September 27 16:40:00 2016', true, 1, 24),
  (10, 'September 27 13:50:00 2016', 'September 27 15:30:00 2016', true, 5, 6),
  (11, 'September 27 13:50:00 2016', 'September 27 17:30:00 2016', true, 2, 2),
  (12, 'September 27 18:40:00 2016', 'September 27 20:20:00 2016', true, 4, 7),
  (13, 'September 27 19:30:00 2016', 'September 26 20:20:00 2016', true, 5, 8),
  -- Dia 28
  (14, 'September 28 08:20:00 2016', 'September 28 12:00:00 2016', true, 2, 9),
  (15, 'September 28 08:20:00 2016', 'September 28 18:00:00 2016', true, 6, 10),
  (16, 'September 28 13:50:00 2016', 'September 28 14:40:00 2016', true, 4, 11),
  (17, 'September 28 13:50:00 2016', 'September 28 18:00:00 2016', true, 3, 17),
  (18, 'September 28 20:30:00 2016', 'September 28 22:00:00 2016', true, 5, 12),
  (28, 'September 28 13:30:00 2016', 'September 29 17:30:00 2016', true, 8, 22),

  -- Dia 29
  (19, 'September 29 08:20:00 2016', 'September 29 12:00:00 2016', true, 5, 13),
  (20, 'September 29 08:20:00 2016', 'September 29 18:00:00 2016', true, 6, 10),
  (27, 'September 29 09:30:00 2016', 'September 29 17:30:00 2016', true, 3, 23),
  (21, 'September 29 13:50:00 2016', 'September 29 14:40:00 2016', true, 4, 21),
  (22, 'September 29 13:50:00 2016', 'September 29 18:00:00 2016', true, 7, 14),
  (23, 'September 29 18:40:00 2016', 'September 29 20:00:00 2016', true, 5, 15),
  -- Dia 30
  (24, 'September 30 08:20:00 2016', 'September 30 12:00:00 2016', true, 4, 16),
  (25, 'September 30 10:20:00 2016', 'September 29 12:00:00 2016', true, 5, 18),
  (26, 'September 30 19:00:00 2016', 'September 29 21:00:00 2016', true, 5, 19);

-- Sync ids no banco
SELECT setval('auth_user_id_seq', COALESCE((SELECT MAX(id)+1 FROM auth_user), 1), false);
SELECT setval('sati_person_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_person), 1), false);
SELECT setval('sati_edition_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_edition), 1), false);
SELECT setval('sati_category_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_category), 1), false);
SELECT setval('sati_event_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_event), 1), false);
SELECT setval('sati_occurrence_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_occurrence), 1), false);
SELECT setval('sati_session_id_seq', COALESCE((SELECT MAX(id)+1 FROM sati_session), 1), false);






