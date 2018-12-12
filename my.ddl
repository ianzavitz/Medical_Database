INSERT INTO hospital (hospital_id,hospital_name) VALUES
(10005,'MARSHALL MEDICAL CENTER SOUTH'),
(10012,'DEKALB REGIONAL MEDICAL CENTER'),
(10095,'HALE COUNTY HOSPITAL'),
(10131,'CRESTWOOD MEDICAL CENTER'),
(11304,'CHOCTAW GENERAL HOSPITAL'),
(20018,'YUKON KUSKOKWIM DELTA REG HOSPITAL'),
(21301,'PROVIDENCE VALDEZ MEDICAL CENTER'),
(21304,'PETERSBURG MEDICAL CENTER'),
(21307,'CORDOVA COMMUNITY MEDICAL CENTER'),
(21308,'NORTON SOUND REGIONAL HOSPITAL'),
(21309,'KANAKANAK HOSPITAL'),
(21310,'MANIILAQ HEALTH CENTER'),
(30071,'FORT DEFIANCE INDIAN HOSPITAL'),
(30073,'TUBA CITY REGIONAL HEALTH CARE CORPORATION'),
(30074,'SELLS HOSPITAL'),
(30077,'SAN CARLOS APACHE HEALTHCARE'),
(30084,'CHINLE COMPREHENSIVE HEALTH CARE FACILITY'),
(31305,'HOPI HEALTH CARE CENTER'),
(31308,'HUHU KAM MEMORIAL HOSPITAL'),
(31309,'SAGE MEMORIAL HOSPITAL'),
(40007,'CHI-ST VINCENT INFIRMARY'),
(40018,'SPARKS MEDICAL CENTER - VAN BUREN'),
(40050,'OUACHITA COUNTY MEDICAL CENTER'),
(40154,'BAPTIST HEALTH MEDICAL CENTER-CONWAY'),
(41328,'CHICOT MEMORIAL MEDICAL CENTER');


INSERT INTO medical_procedure VALUES
   (4234,'Excision_of_Abdominal_Aorta_Open_Approach'),
   (4235,'Excision of Abdominal Aorta, Percutaneous Endoscopic Approach'),
   (4236,'Replacement of Abdominal Aorta with Autologous Tissue Substitute, Open Approach'),
   (4237,'Replacement of Abdominal Aorta with Synthetic Substitute, Open Approach'),
   (4238,'Replacement of Abdominal Aorta with Nonautologous Tissue Substitute, Open Approach'),
   (4239,'Replacement of Abdominal Aorta with Autologous Tissue Substitute, Percutaneous Endoscopic Approach'),
   (4240,'Replacement of Abdominal Aorta with Synthetic Substitute, Percutaneous Endoscopic Approach'),
   (4241,'Replacement of Abdominal Aorta with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach'),
   (4242,'Detachment at Right Forequarter, Open Approach'),
   (4243,'Detachment at Left Forequarter, Open Approach'),
   (4244,'Detachment at Right Shoulder Region, Open Approach'),
   (4245,'Detachment at Left Shoulder Region, Open Approach'),
   (4246,'Detachment at Right Upper Arm, High, Open Approach'),
   (4247,'Detachment at Right Upper Arm, Mid, Open Approach'),
   (4248,'Detachment at Right Upper Arm, Low, Open Approach'),
   (4249,'Detachment at Left Upper Arm, High, Open Approach'),
   (4250,'Detachment at Left Upper Arm, Mid, Open Approach'),
   (4251,'Detachment at Left Upper Arm, Low, Open Approach'),
   (4252,'Detachment at Right Elbow Region, Open Approach'),
   (4253,'Detachment at Left Elbow Region, Open Approach'),
   (4254,'Detachment at Right Lower Arm, High, Open Approach'),
   (4255,'Detachment at Right Lower Arm, Mid, Open Approach'),
   (4256,'Detachment at Right Lower Arm, Low, Open Approach'),
   (4257,'Detachment at Left Lower Arm, High, Open Approach'),
   (4258,'Detachment at Left Lower Arm, Mid, Open Approach'),
   (4259,'Detachment at Left Lower Arm, Low, Open Approach'),
   (4260,'Detachment at Right Hand, Complete, Open Approach'),
   (4261,'Detachment at Right Hand, Complete 1st Ray, Open Approach'),
   (4262,'Detachment at Right Hand, Complete 2nd Ray, Open Approach'),
   (4263,'Detachment at Right Hand, Complete 3rd Ray, Open Approach'),
   (4264,'Detachment at Right Hand, Complete 4th Ray, Open Approach'),
   (4265,'Detachment at Right Hand, Complete 5th Ray, Open Approach'),
   (4266,'Detachment at Right Hand, Partial 1st Ray, Open Approach'),
   (4267,'Detachment at Right Hand, Partial 2nd Ray, Open Approach'),
   (4268,'Detachment at Right Hand, Partial 3rd Ray, Open Approach'),
   (4269,'Detachment at Right Hand, Partial 4th Ray, Open Approach'),
   (4270,'Detachment at Right Hand, Partial 5th Ray, Open Approach'),
   (4271,'Detachment at Left Hand, Complete, Open Approach'),
   (4272,'Detachment at Left Hand, Complete 1st Ray, Open Approach'),
   (4273,'Detachment at Left Hand, Complete 2nd Ray, Open Approach'),
   (4274,'Detachment at Left Hand, Complete 3rd Ray, Open Approach'),
   (4275,'Detachment at Left Hand, Complete 4th Ray, Open Approach'),
   (4276,'Detachment at Left Hand, Complete 5th Ray, Open Approach'),
   (4277,'Detachment at Left Hand, Partial 1st Ray, Open Approach'),
   (4278,'Detachment at Left Hand, Partial 2nd Ray, Open Approach'),
   (4279,'Detachment at Left Hand, Partial 3rd Ray, Open Approach'),
   (4280,'Detachment at Left Hand, Partial 4th Ray, Open Approach'),
   (4281,'Detachment at Left Hand, Partial 5th Ray, Open Approach'),
   (4282,'Detachment at Right Thumb, Complete, Open Approach');

   
INSERT INTO physician(hospital_id_FK,physician_id,physician_last_name) VALUES
(10005,11424,"Elvira"),
(10005,11426,"Fallon"),
(10005,11428,"Enola"),
(10131,11430,"Titus"),
(11304,11432,"Buffy"),
(20018,11434,"Nathalie"),
(20018,11436,"Divina"),
(20018,11438,"Rosalind"),
(20018,11440,"See"),
(20018,11442,"Alica"),
(20018,11444,"Vida"),
(21310,11446,"Kenisha"),
(30071,11448,"Sherly"),
(30073,11450,"Silvana"),
(30074,11452,"Siobhan"),
(30077,11454,"Burt"),
(30084,11456,"Eusebio"),
(31305,11458,"Monet"),
(31308,11460,"Letty"),
(31309,11462,"Mei"),
(40007,11464,"Kawasaki"),
(40018,11466,"Ronaldo"),
(40050,11468,"Raimundo"),
(40154,11470,"Mode"),
(41328,11472,"Spiderman")


INSERT INTO patient(patient_id,age,diagnosis) VALUES
(1,22,"Ugliness");

INSERT INTO medical_case(medical_case.case_id,medical_case.patient_id_FK,medical_case.procedure_id_FK,medical_case.outcome,medical_case.stay_duration) VALUES
(1,1,4234,"positive",3);
UPDATE patient SET case_id_FK = 1 WHERE patient_id = 1