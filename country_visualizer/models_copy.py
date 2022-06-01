# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answers(models.Model):
    q = models.TextField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    subtheme = models.TextField(blank=True, null=True)
    alt_op_5 = models.TextField(blank=True, null=True)
    alt_op_4 = models.TextField(blank=True, null=True)
    alt_op_3 = models.TextField(blank=True, null=True)
    alt_op_2 = models.TextField(blank=True, null=True)
    alt_op_1 = models.TextField(blank=True, null=True)
    op_1 = models.TextField(blank=True, null=True)
    op_2 = models.TextField(blank=True, null=True)
    op_3 = models.TextField(blank=True, null=True)
    op_4 = models.TextField(blank=True, null=True)
    op_5 = models.TextField(blank=True, null=True)
    op_6 = models.TextField(blank=True, null=True)
    op_7 = models.TextField(blank=True, null=True)
    op_8 = models.TextField(blank=True, null=True)
    op_9 = models.TextField(blank=True, null=True)
    op_10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class ApiPopulation(models.Model):
    id = models.BigAutoField(primary_key=True)
    population = models.CharField(max_length=80)
    avg_age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_population'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Questions(models.Model):
    version = models.TextField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    a_wave = models.TextField(db_column='A_WAVE', blank=True, null=True)  # Field name made lowercase.
    a_study = models.TextField(db_column='A_STUDY', blank=True, null=True)  # Field name made lowercase.
    b_country = models.TextField(db_column='B_COUNTRY', blank=True, null=True)  # Field name made lowercase.
    b_country_alpha = models.TextField(db_column='B_COUNTRY_ALPHA', blank=True, null=True)  # Field name made lowercase.
    c_cow_num = models.TextField(db_column='C_COW_NUM', blank=True, null=True)  # Field name made lowercase.
    c_cow_alpha = models.TextField(db_column='C_COW_ALPHA', blank=True, null=True)  # Field name made lowercase.
    a_year = models.TextField(db_column='A_YEAR', blank=True, null=True)  # Field name made lowercase.
    d_interview = models.TextField(db_column='D_INTERVIEW', blank=True, null=True)  # Field name made lowercase.
    j_intdate = models.TextField(db_column='J_INTDATE', blank=True, null=True)  # Field name made lowercase.
    fw_end = models.TextField(db_column='FW_END', blank=True, null=True)  # Field name made lowercase.
    fw_start = models.TextField(db_column='FW_START', blank=True, null=True)  # Field name made lowercase.
    k_time_start = models.TextField(db_column='K_TIME_START', blank=True, null=True)  # Field name made lowercase.
    k_time_end = models.TextField(db_column='K_TIME_END', blank=True, null=True)  # Field name made lowercase.
    k_duration = models.TextField(db_column='K_DURATION', blank=True, null=True)  # Field name made lowercase.
    q_mode = models.TextField(db_column='Q_MODE', blank=True, null=True)  # Field name made lowercase.
    n_region_iso = models.TextField(db_column='N_REGION_ISO', blank=True, null=True)  # Field name made lowercase.
    n_region_wvs = models.TextField(db_column='N_REGION_WVS', blank=True, null=True)  # Field name made lowercase.
    n_town = models.TextField(db_column='N_TOWN', blank=True, null=True)  # Field name made lowercase.
    g_townsize = models.TextField(db_column='G_TOWNSIZE', blank=True, null=True)  # Field name made lowercase.
    g_townsize2 = models.TextField(db_column='G_TOWNSIZE2', blank=True, null=True)  # Field name made lowercase.
    h_settlement = models.TextField(db_column='H_SETTLEMENT', blank=True, null=True)  # Field name made lowercase.
    h_urbrural = models.TextField(db_column='H_URBRURAL', blank=True, null=True)  # Field name made lowercase.
    i_psu = models.TextField(db_column='I_PSU', blank=True, null=True)  # Field name made lowercase.
    o1_longitude = models.TextField(db_column='O1_LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    o2_latitude = models.TextField(db_column='O2_LATITUDE', blank=True, null=True)  # Field name made lowercase.
    s_intlanguage = models.TextField(db_column='S_INTLANGUAGE', blank=True, null=True)  # Field name made lowercase.
    lnge_iso = models.TextField(db_column='LNGE_ISO', blank=True, null=True)  # Field name made lowercase.
    e_respint = models.TextField(db_column='E_RESPINT', blank=True, null=True)  # Field name made lowercase.
    f_intprivacy = models.TextField(db_column='F_INTPRIVACY', blank=True, null=True)  # Field name made lowercase.
    e1_literacy = models.TextField(db_column='E1_LITERACY', blank=True, null=True)  # Field name made lowercase.
    w_weight = models.TextField(db_column='W_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    s018 = models.TextField(db_column='S018', blank=True, null=True)  # Field name made lowercase.
    pwght = models.TextField(db_column='PWGHT', blank=True, null=True)  # Field name made lowercase.
    s025 = models.TextField(db_column='S025', blank=True, null=True)  # Field name made lowercase.
    q1 = models.TextField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.TextField(db_column='Q2', blank=True, null=True)  # Field name made lowercase.
    q3 = models.TextField(db_column='Q3', blank=True, null=True)  # Field name made lowercase.
    q4 = models.TextField(db_column='Q4', blank=True, null=True)  # Field name made lowercase.
    q5 = models.TextField(db_column='Q5', blank=True, null=True)  # Field name made lowercase.
    q6 = models.TextField(db_column='Q6', blank=True, null=True)  # Field name made lowercase.
    q7 = models.TextField(db_column='Q7', blank=True, null=True)  # Field name made lowercase.
    q8 = models.TextField(db_column='Q8', blank=True, null=True)  # Field name made lowercase.
    q9 = models.TextField(db_column='Q9', blank=True, null=True)  # Field name made lowercase.
    q10 = models.TextField(db_column='Q10', blank=True, null=True)  # Field name made lowercase.
    q11 = models.TextField(db_column='Q11', blank=True, null=True)  # Field name made lowercase.
    q12 = models.TextField(db_column='Q12', blank=True, null=True)  # Field name made lowercase.
    q13 = models.TextField(db_column='Q13', blank=True, null=True)  # Field name made lowercase.
    q14 = models.TextField(db_column='Q14', blank=True, null=True)  # Field name made lowercase.
    q15 = models.TextField(db_column='Q15', blank=True, null=True)  # Field name made lowercase.
    q16 = models.TextField(db_column='Q16', blank=True, null=True)  # Field name made lowercase.
    q17 = models.TextField(db_column='Q17', blank=True, null=True)  # Field name made lowercase.
    q18 = models.TextField(db_column='Q18', blank=True, null=True)  # Field name made lowercase.
    q19 = models.TextField(db_column='Q19', blank=True, null=True)  # Field name made lowercase.
    q20 = models.TextField(db_column='Q20', blank=True, null=True)  # Field name made lowercase.
    q21 = models.TextField(db_column='Q21', blank=True, null=True)  # Field name made lowercase.
    q22 = models.TextField(db_column='Q22', blank=True, null=True)  # Field name made lowercase.
    q23 = models.TextField(db_column='Q23', blank=True, null=True)  # Field name made lowercase.
    q24 = models.TextField(db_column='Q24', blank=True, null=True)  # Field name made lowercase.
    q25 = models.TextField(db_column='Q25', blank=True, null=True)  # Field name made lowercase.
    q26 = models.TextField(db_column='Q26', blank=True, null=True)  # Field name made lowercase.
    q27 = models.TextField(db_column='Q27', blank=True, null=True)  # Field name made lowercase.
    q28 = models.TextField(db_column='Q28', blank=True, null=True)  # Field name made lowercase.
    q29 = models.TextField(db_column='Q29', blank=True, null=True)  # Field name made lowercase.
    q30 = models.TextField(db_column='Q30', blank=True, null=True)  # Field name made lowercase.
    q31 = models.TextField(db_column='Q31', blank=True, null=True)  # Field name made lowercase.
    q32 = models.TextField(db_column='Q32', blank=True, null=True)  # Field name made lowercase.
    q33 = models.TextField(db_column='Q33', blank=True, null=True)  # Field name made lowercase.
    q33_3 = models.TextField(db_column='Q33_3', blank=True, null=True)  # Field name made lowercase.
    q34 = models.TextField(db_column='Q34', blank=True, null=True)  # Field name made lowercase.
    q34_3 = models.TextField(db_column='Q34_3', blank=True, null=True)  # Field name made lowercase.
    q35 = models.TextField(db_column='Q35', blank=True, null=True)  # Field name made lowercase.
    q35_3 = models.TextField(db_column='Q35_3', blank=True, null=True)  # Field name made lowercase.
    q36 = models.TextField(db_column='Q36', blank=True, null=True)  # Field name made lowercase.
    q37 = models.TextField(db_column='Q37', blank=True, null=True)  # Field name made lowercase.
    q38 = models.TextField(db_column='Q38', blank=True, null=True)  # Field name made lowercase.
    q39 = models.TextField(db_column='Q39', blank=True, null=True)  # Field name made lowercase.
    q40 = models.TextField(db_column='Q40', blank=True, null=True)  # Field name made lowercase.
    q41 = models.TextField(db_column='Q41', blank=True, null=True)  # Field name made lowercase.
    q42 = models.TextField(db_column='Q42', blank=True, null=True)  # Field name made lowercase.
    q43 = models.TextField(db_column='Q43', blank=True, null=True)  # Field name made lowercase.
    q44 = models.TextField(db_column='Q44', blank=True, null=True)  # Field name made lowercase.
    q45 = models.TextField(db_column='Q45', blank=True, null=True)  # Field name made lowercase.
    q46 = models.TextField(db_column='Q46', blank=True, null=True)  # Field name made lowercase.
    q47 = models.TextField(db_column='Q47', blank=True, null=True)  # Field name made lowercase.
    q48 = models.TextField(db_column='Q48', blank=True, null=True)  # Field name made lowercase.
    q49 = models.TextField(db_column='Q49', blank=True, null=True)  # Field name made lowercase.
    q50 = models.TextField(db_column='Q50', blank=True, null=True)  # Field name made lowercase.
    q51 = models.TextField(db_column='Q51', blank=True, null=True)  # Field name made lowercase.
    q52 = models.TextField(db_column='Q52', blank=True, null=True)  # Field name made lowercase.
    q53 = models.TextField(db_column='Q53', blank=True, null=True)  # Field name made lowercase.
    q54 = models.TextField(db_column='Q54', blank=True, null=True)  # Field name made lowercase.
    q55 = models.TextField(db_column='Q55', blank=True, null=True)  # Field name made lowercase.
    q56 = models.TextField(db_column='Q56', blank=True, null=True)  # Field name made lowercase.
    q57 = models.TextField(db_column='Q57', blank=True, null=True)  # Field name made lowercase.
    q58 = models.TextField(db_column='Q58', blank=True, null=True)  # Field name made lowercase.
    q59 = models.TextField(db_column='Q59', blank=True, null=True)  # Field name made lowercase.
    q60 = models.TextField(db_column='Q60', blank=True, null=True)  # Field name made lowercase.
    q61 = models.TextField(db_column='Q61', blank=True, null=True)  # Field name made lowercase.
    q62 = models.TextField(db_column='Q62', blank=True, null=True)  # Field name made lowercase.
    q63 = models.TextField(db_column='Q63', blank=True, null=True)  # Field name made lowercase.
    q64 = models.TextField(db_column='Q64', blank=True, null=True)  # Field name made lowercase.
    q65 = models.TextField(db_column='Q65', blank=True, null=True)  # Field name made lowercase.
    q66 = models.TextField(db_column='Q66', blank=True, null=True)  # Field name made lowercase.
    q67 = models.TextField(db_column='Q67', blank=True, null=True)  # Field name made lowercase.
    q68 = models.TextField(db_column='Q68', blank=True, null=True)  # Field name made lowercase.
    q69 = models.TextField(db_column='Q69', blank=True, null=True)  # Field name made lowercase.
    q70 = models.TextField(db_column='Q70', blank=True, null=True)  # Field name made lowercase.
    q71 = models.TextField(db_column='Q71', blank=True, null=True)  # Field name made lowercase.
    q72 = models.TextField(db_column='Q72', blank=True, null=True)  # Field name made lowercase.
    q73 = models.TextField(db_column='Q73', blank=True, null=True)  # Field name made lowercase.
    q74 = models.TextField(db_column='Q74', blank=True, null=True)  # Field name made lowercase.
    q75 = models.TextField(db_column='Q75', blank=True, null=True)  # Field name made lowercase.
    q76 = models.TextField(db_column='Q76', blank=True, null=True)  # Field name made lowercase.
    q77 = models.TextField(db_column='Q77', blank=True, null=True)  # Field name made lowercase.
    q78 = models.TextField(db_column='Q78', blank=True, null=True)  # Field name made lowercase.
    q79 = models.TextField(db_column='Q79', blank=True, null=True)  # Field name made lowercase.
    q80 = models.TextField(db_column='Q80', blank=True, null=True)  # Field name made lowercase.
    q81 = models.TextField(db_column='Q81', blank=True, null=True)  # Field name made lowercase.
    q82 = models.TextField(db_column='Q82', blank=True, null=True)  # Field name made lowercase.
    q82_eu = models.TextField(db_column='Q82_EU', blank=True, null=True)  # Field name made lowercase.
    q82_apec = models.TextField(db_column='Q82_APEC', blank=True, null=True)  # Field name made lowercase.
    q82_arableague = models.TextField(db_column='Q82_ARABLEAGUE', blank=True, null=True)  # Field name made lowercase.
    q82_asean = models.TextField(db_column='Q82_ASEAN', blank=True, null=True)  # Field name made lowercase.
    q82_africanunion = models.TextField(db_column='Q82_AFRICANUNION', blank=True, null=True)  # Field name made lowercase.
    q82_cis = models.TextField(db_column='Q82_CIS', blank=True, null=True)  # Field name made lowercase.
    q82_eco = models.TextField(db_column='Q82_ECO', blank=True, null=True)  # Field name made lowercase.
    q82_gulfcoop = models.TextField(db_column='Q82_GULFCOOP', blank=True, null=True)  # Field name made lowercase.
    q82_islcoop = models.TextField(db_column='Q82_ISLCOOP', blank=True, null=True)  # Field name made lowercase.
    q82_mercosur = models.TextField(db_column='Q82_MERCOSUR', blank=True, null=True)  # Field name made lowercase.
    q82_nafta = models.TextField(db_column='Q82_NAFTA', blank=True, null=True)  # Field name made lowercase.
    q82_oas = models.TextField(db_column='Q82_OAS', blank=True, null=True)  # Field name made lowercase.
    q82_saarc = models.TextField(db_column='Q82_SAARC', blank=True, null=True)  # Field name made lowercase.
    q82_sco = models.TextField(db_column='Q82_SCO', blank=True, null=True)  # Field name made lowercase.
    q82_tlc = models.TextField(db_column='Q82_TLC', blank=True, null=True)  # Field name made lowercase.
    q82_undp = models.TextField(db_column='Q82_UNDP', blank=True, null=True)  # Field name made lowercase.
    q83 = models.TextField(db_column='Q83', blank=True, null=True)  # Field name made lowercase.
    q84 = models.TextField(db_column='Q84', blank=True, null=True)  # Field name made lowercase.
    q85 = models.TextField(db_column='Q85', blank=True, null=True)  # Field name made lowercase.
    q86 = models.TextField(db_column='Q86', blank=True, null=True)  # Field name made lowercase.
    q87 = models.TextField(db_column='Q87', blank=True, null=True)  # Field name made lowercase.
    q88 = models.TextField(db_column='Q88', blank=True, null=True)  # Field name made lowercase.
    q89 = models.TextField(db_column='Q89', blank=True, null=True)  # Field name made lowercase.
    q90 = models.TextField(db_column='Q90', blank=True, null=True)  # Field name made lowercase.
    q91 = models.TextField(db_column='Q91', blank=True, null=True)  # Field name made lowercase.
    q92 = models.TextField(db_column='Q92', blank=True, null=True)  # Field name made lowercase.
    q93 = models.TextField(db_column='Q93', blank=True, null=True)  # Field name made lowercase.
    q94 = models.TextField(db_column='Q94', blank=True, null=True)  # Field name made lowercase.
    q95 = models.TextField(db_column='Q95', blank=True, null=True)  # Field name made lowercase.
    q96 = models.TextField(db_column='Q96', blank=True, null=True)  # Field name made lowercase.
    q97 = models.TextField(db_column='Q97', blank=True, null=True)  # Field name made lowercase.
    q98 = models.TextField(db_column='Q98', blank=True, null=True)  # Field name made lowercase.
    q99 = models.TextField(db_column='Q99', blank=True, null=True)  # Field name made lowercase.
    q100 = models.TextField(db_column='Q100', blank=True, null=True)  # Field name made lowercase.
    q101 = models.TextField(db_column='Q101', blank=True, null=True)  # Field name made lowercase.
    q102 = models.TextField(db_column='Q102', blank=True, null=True)  # Field name made lowercase.
    q103 = models.TextField(db_column='Q103', blank=True, null=True)  # Field name made lowercase.
    q104 = models.TextField(db_column='Q104', blank=True, null=True)  # Field name made lowercase.
    q105 = models.TextField(db_column='Q105', blank=True, null=True)  # Field name made lowercase.
    q106 = models.TextField(db_column='Q106', blank=True, null=True)  # Field name made lowercase.
    q107 = models.TextField(db_column='Q107', blank=True, null=True)  # Field name made lowercase.
    q108 = models.TextField(db_column='Q108', blank=True, null=True)  # Field name made lowercase.
    q109 = models.TextField(db_column='Q109', blank=True, null=True)  # Field name made lowercase.
    q110 = models.TextField(db_column='Q110', blank=True, null=True)  # Field name made lowercase.
    q111 = models.TextField(db_column='Q111', blank=True, null=True)  # Field name made lowercase.
    q112 = models.TextField(db_column='Q112', blank=True, null=True)  # Field name made lowercase.
    q113 = models.TextField(db_column='Q113', blank=True, null=True)  # Field name made lowercase.
    q114 = models.TextField(db_column='Q114', blank=True, null=True)  # Field name made lowercase.
    q115 = models.TextField(db_column='Q115', blank=True, null=True)  # Field name made lowercase.
    q116 = models.TextField(db_column='Q116', blank=True, null=True)  # Field name made lowercase.
    q117 = models.TextField(db_column='Q117', blank=True, null=True)  # Field name made lowercase.
    q118 = models.TextField(db_column='Q118', blank=True, null=True)  # Field name made lowercase.
    q119 = models.TextField(db_column='Q119', blank=True, null=True)  # Field name made lowercase.
    q120 = models.TextField(db_column='Q120', blank=True, null=True)  # Field name made lowercase.
    q121 = models.TextField(db_column='Q121', blank=True, null=True)  # Field name made lowercase.
    q122 = models.TextField(db_column='Q122', blank=True, null=True)  # Field name made lowercase.
    q123 = models.TextField(db_column='Q123', blank=True, null=True)  # Field name made lowercase.
    q124 = models.TextField(db_column='Q124', blank=True, null=True)  # Field name made lowercase.
    q125 = models.TextField(db_column='Q125', blank=True, null=True)  # Field name made lowercase.
    q126 = models.TextField(db_column='Q126', blank=True, null=True)  # Field name made lowercase.
    q127 = models.TextField(db_column='Q127', blank=True, null=True)  # Field name made lowercase.
    q128 = models.TextField(db_column='Q128', blank=True, null=True)  # Field name made lowercase.
    q129 = models.TextField(db_column='Q129', blank=True, null=True)  # Field name made lowercase.
    q130 = models.TextField(db_column='Q130', blank=True, null=True)  # Field name made lowercase.
    q131 = models.TextField(db_column='Q131', blank=True, null=True)  # Field name made lowercase.
    q132 = models.TextField(db_column='Q132', blank=True, null=True)  # Field name made lowercase.
    q133 = models.TextField(db_column='Q133', blank=True, null=True)  # Field name made lowercase.
    q134 = models.TextField(db_column='Q134', blank=True, null=True)  # Field name made lowercase.
    q135 = models.TextField(db_column='Q135', blank=True, null=True)  # Field name made lowercase.
    q136 = models.TextField(db_column='Q136', blank=True, null=True)  # Field name made lowercase.
    q137 = models.TextField(db_column='Q137', blank=True, null=True)  # Field name made lowercase.
    q138 = models.TextField(db_column='Q138', blank=True, null=True)  # Field name made lowercase.
    q139 = models.TextField(db_column='Q139', blank=True, null=True)  # Field name made lowercase.
    q140 = models.TextField(db_column='Q140', blank=True, null=True)  # Field name made lowercase.
    q141 = models.TextField(db_column='Q141', blank=True, null=True)  # Field name made lowercase.
    q142 = models.TextField(db_column='Q142', blank=True, null=True)  # Field name made lowercase.
    q143 = models.TextField(db_column='Q143', blank=True, null=True)  # Field name made lowercase.
    q144 = models.TextField(db_column='Q144', blank=True, null=True)  # Field name made lowercase.
    q145 = models.TextField(db_column='Q145', blank=True, null=True)  # Field name made lowercase.
    q146 = models.TextField(db_column='Q146', blank=True, null=True)  # Field name made lowercase.
    q147 = models.TextField(db_column='Q147', blank=True, null=True)  # Field name made lowercase.
    q148 = models.TextField(db_column='Q148', blank=True, null=True)  # Field name made lowercase.
    q149 = models.TextField(db_column='Q149', blank=True, null=True)  # Field name made lowercase.
    q150 = models.TextField(db_column='Q150', blank=True, null=True)  # Field name made lowercase.
    q151 = models.TextField(db_column='Q151', blank=True, null=True)  # Field name made lowercase.
    q152 = models.TextField(db_column='Q152', blank=True, null=True)  # Field name made lowercase.
    q153 = models.TextField(db_column='Q153', blank=True, null=True)  # Field name made lowercase.
    q154 = models.TextField(db_column='Q154', blank=True, null=True)  # Field name made lowercase.
    q155 = models.TextField(db_column='Q155', blank=True, null=True)  # Field name made lowercase.
    q156 = models.TextField(db_column='Q156', blank=True, null=True)  # Field name made lowercase.
    q157 = models.TextField(db_column='Q157', blank=True, null=True)  # Field name made lowercase.
    q158 = models.TextField(db_column='Q158', blank=True, null=True)  # Field name made lowercase.
    q159 = models.TextField(db_column='Q159', blank=True, null=True)  # Field name made lowercase.
    q160 = models.TextField(db_column='Q160', blank=True, null=True)  # Field name made lowercase.
    q161 = models.TextField(db_column='Q161', blank=True, null=True)  # Field name made lowercase.
    q162 = models.TextField(db_column='Q162', blank=True, null=True)  # Field name made lowercase.
    q163 = models.TextField(db_column='Q163', blank=True, null=True)  # Field name made lowercase.
    q164 = models.TextField(db_column='Q164', blank=True, null=True)  # Field name made lowercase.
    q165 = models.TextField(db_column='Q165', blank=True, null=True)  # Field name made lowercase.
    q166 = models.TextField(db_column='Q166', blank=True, null=True)  # Field name made lowercase.
    q167 = models.TextField(db_column='Q167', blank=True, null=True)  # Field name made lowercase.
    q168 = models.TextField(db_column='Q168', blank=True, null=True)  # Field name made lowercase.
    q169 = models.TextField(db_column='Q169', blank=True, null=True)  # Field name made lowercase.
    q170 = models.TextField(db_column='Q170', blank=True, null=True)  # Field name made lowercase.
    q171 = models.TextField(db_column='Q171', blank=True, null=True)  # Field name made lowercase.
    q172 = models.TextField(db_column='Q172', blank=True, null=True)  # Field name made lowercase.
    q173 = models.TextField(db_column='Q173', blank=True, null=True)  # Field name made lowercase.
    q174 = models.TextField(db_column='Q174', blank=True, null=True)  # Field name made lowercase.
    q175 = models.TextField(db_column='Q175', blank=True, null=True)  # Field name made lowercase.
    q176 = models.TextField(db_column='Q176', blank=True, null=True)  # Field name made lowercase.
    q177 = models.TextField(db_column='Q177', blank=True, null=True)  # Field name made lowercase.
    q178 = models.TextField(db_column='Q178', blank=True, null=True)  # Field name made lowercase.
    q179 = models.TextField(db_column='Q179', blank=True, null=True)  # Field name made lowercase.
    q180 = models.TextField(db_column='Q180', blank=True, null=True)  # Field name made lowercase.
    q181 = models.TextField(db_column='Q181', blank=True, null=True)  # Field name made lowercase.
    q182 = models.TextField(db_column='Q182', blank=True, null=True)  # Field name made lowercase.
    q183 = models.TextField(db_column='Q183', blank=True, null=True)  # Field name made lowercase.
    q184 = models.TextField(db_column='Q184', blank=True, null=True)  # Field name made lowercase.
    q185 = models.TextField(db_column='Q185', blank=True, null=True)  # Field name made lowercase.
    q186 = models.TextField(db_column='Q186', blank=True, null=True)  # Field name made lowercase.
    q187 = models.TextField(db_column='Q187', blank=True, null=True)  # Field name made lowercase.
    q188 = models.TextField(db_column='Q188', blank=True, null=True)  # Field name made lowercase.
    q189 = models.TextField(db_column='Q189', blank=True, null=True)  # Field name made lowercase.
    q190 = models.TextField(db_column='Q190', blank=True, null=True)  # Field name made lowercase.
    q191 = models.TextField(db_column='Q191', blank=True, null=True)  # Field name made lowercase.
    q192 = models.TextField(db_column='Q192', blank=True, null=True)  # Field name made lowercase.
    q193 = models.TextField(db_column='Q193', blank=True, null=True)  # Field name made lowercase.
    q194 = models.TextField(db_column='Q194', blank=True, null=True)  # Field name made lowercase.
    q195 = models.TextField(db_column='Q195', blank=True, null=True)  # Field name made lowercase.
    q196 = models.TextField(db_column='Q196', blank=True, null=True)  # Field name made lowercase.
    q197 = models.TextField(db_column='Q197', blank=True, null=True)  # Field name made lowercase.
    q198 = models.TextField(db_column='Q198', blank=True, null=True)  # Field name made lowercase.
    q199 = models.TextField(db_column='Q199', blank=True, null=True)  # Field name made lowercase.
    q200 = models.TextField(db_column='Q200', blank=True, null=True)  # Field name made lowercase.
    q201 = models.TextField(db_column='Q201', blank=True, null=True)  # Field name made lowercase.
    q202 = models.TextField(db_column='Q202', blank=True, null=True)  # Field name made lowercase.
    q203 = models.TextField(db_column='Q203', blank=True, null=True)  # Field name made lowercase.
    q204 = models.TextField(db_column='Q204', blank=True, null=True)  # Field name made lowercase.
    q205 = models.TextField(db_column='Q205', blank=True, null=True)  # Field name made lowercase.
    q206 = models.TextField(db_column='Q206', blank=True, null=True)  # Field name made lowercase.
    q207 = models.TextField(db_column='Q207', blank=True, null=True)  # Field name made lowercase.
    q208 = models.TextField(db_column='Q208', blank=True, null=True)  # Field name made lowercase.
    q209 = models.TextField(db_column='Q209', blank=True, null=True)  # Field name made lowercase.
    q210 = models.TextField(db_column='Q210', blank=True, null=True)  # Field name made lowercase.
    q211 = models.TextField(db_column='Q211', blank=True, null=True)  # Field name made lowercase.
    q212 = models.TextField(db_column='Q212', blank=True, null=True)  # Field name made lowercase.
    q213 = models.TextField(db_column='Q213', blank=True, null=True)  # Field name made lowercase.
    q214 = models.TextField(db_column='Q214', blank=True, null=True)  # Field name made lowercase.
    q215 = models.TextField(db_column='Q215', blank=True, null=True)  # Field name made lowercase.
    q216 = models.TextField(db_column='Q216', blank=True, null=True)  # Field name made lowercase.
    q217 = models.TextField(db_column='Q217', blank=True, null=True)  # Field name made lowercase.
    q218 = models.TextField(db_column='Q218', blank=True, null=True)  # Field name made lowercase.
    q219 = models.TextField(db_column='Q219', blank=True, null=True)  # Field name made lowercase.
    q220 = models.TextField(db_column='Q220', blank=True, null=True)  # Field name made lowercase.
    q221 = models.TextField(db_column='Q221', blank=True, null=True)  # Field name made lowercase.
    q222 = models.TextField(db_column='Q222', blank=True, null=True)  # Field name made lowercase.
    q223 = models.TextField(db_column='Q223', blank=True, null=True)  # Field name made lowercase.
    q223_abrev = models.TextField(db_column='Q223_ABREV', blank=True, null=True)  # Field name made lowercase.
    q223_local = models.TextField(db_column='Q223_LOCAL', blank=True, null=True)  # Field name made lowercase.
    q224 = models.TextField(db_column='Q224', blank=True, null=True)  # Field name made lowercase.
    q225 = models.TextField(db_column='Q225', blank=True, null=True)  # Field name made lowercase.
    q226 = models.TextField(db_column='Q226', blank=True, null=True)  # Field name made lowercase.
    q227 = models.TextField(db_column='Q227', blank=True, null=True)  # Field name made lowercase.
    q228 = models.TextField(db_column='Q228', blank=True, null=True)  # Field name made lowercase.
    q229 = models.TextField(db_column='Q229', blank=True, null=True)  # Field name made lowercase.
    q230 = models.TextField(db_column='Q230', blank=True, null=True)  # Field name made lowercase.
    q231 = models.TextField(db_column='Q231', blank=True, null=True)  # Field name made lowercase.
    q232 = models.TextField(db_column='Q232', blank=True, null=True)  # Field name made lowercase.
    q233 = models.TextField(db_column='Q233', blank=True, null=True)  # Field name made lowercase.
    q234 = models.TextField(db_column='Q234', blank=True, null=True)  # Field name made lowercase.
    q234a = models.TextField(db_column='Q234A', blank=True, null=True)  # Field name made lowercase.
    q235 = models.TextField(db_column='Q235', blank=True, null=True)  # Field name made lowercase.
    q236 = models.TextField(db_column='Q236', blank=True, null=True)  # Field name made lowercase.
    q237 = models.TextField(db_column='Q237', blank=True, null=True)  # Field name made lowercase.
    q238 = models.TextField(db_column='Q238', blank=True, null=True)  # Field name made lowercase.
    q239 = models.TextField(db_column='Q239', blank=True, null=True)  # Field name made lowercase.
    q240 = models.TextField(db_column='Q240', blank=True, null=True)  # Field name made lowercase.
    q241 = models.TextField(db_column='Q241', blank=True, null=True)  # Field name made lowercase.
    q242 = models.TextField(db_column='Q242', blank=True, null=True)  # Field name made lowercase.
    q243 = models.TextField(db_column='Q243', blank=True, null=True)  # Field name made lowercase.
    q244 = models.TextField(db_column='Q244', blank=True, null=True)  # Field name made lowercase.
    q245 = models.TextField(db_column='Q245', blank=True, null=True)  # Field name made lowercase.
    q246 = models.TextField(db_column='Q246', blank=True, null=True)  # Field name made lowercase.
    q247 = models.TextField(db_column='Q247', blank=True, null=True)  # Field name made lowercase.
    q248 = models.TextField(db_column='Q248', blank=True, null=True)  # Field name made lowercase.
    q249 = models.TextField(db_column='Q249', blank=True, null=True)  # Field name made lowercase.
    q250 = models.TextField(db_column='Q250', blank=True, null=True)  # Field name made lowercase.
    q251 = models.TextField(db_column='Q251', blank=True, null=True)  # Field name made lowercase.
    q252 = models.TextField(db_column='Q252', blank=True, null=True)  # Field name made lowercase.
    q253 = models.TextField(db_column='Q253', blank=True, null=True)  # Field name made lowercase.
    q254 = models.TextField(db_column='Q254', blank=True, null=True)  # Field name made lowercase.
    q255 = models.TextField(db_column='Q255', blank=True, null=True)  # Field name made lowercase.
    q256 = models.TextField(db_column='Q256', blank=True, null=True)  # Field name made lowercase.
    q257 = models.TextField(db_column='Q257', blank=True, null=True)  # Field name made lowercase.
    q258 = models.TextField(db_column='Q258', blank=True, null=True)  # Field name made lowercase.
    q259 = models.TextField(db_column='Q259', blank=True, null=True)  # Field name made lowercase.
    q260 = models.TextField(db_column='Q260', blank=True, null=True)  # Field name made lowercase.
    q261 = models.TextField(db_column='Q261', blank=True, null=True)  # Field name made lowercase.
    q262 = models.TextField(db_column='Q262', blank=True, null=True)  # Field name made lowercase.
    x003r2 = models.TextField(db_column='X003R2', blank=True, null=True)  # Field name made lowercase.
    x003r = models.TextField(blank=True, null=True)
    q263 = models.TextField(db_column='Q263', blank=True, null=True)  # Field name made lowercase.
    q264 = models.TextField(db_column='Q264', blank=True, null=True)  # Field name made lowercase.
    q265 = models.TextField(db_column='Q265', blank=True, null=True)  # Field name made lowercase.
    q266 = models.TextField(db_column='Q266', blank=True, null=True)  # Field name made lowercase.
    q267 = models.TextField(db_column='Q267', blank=True, null=True)  # Field name made lowercase.
    q268 = models.TextField(db_column='Q268', blank=True, null=True)  # Field name made lowercase.
    q269 = models.TextField(db_column='Q269', blank=True, null=True)  # Field name made lowercase.
    q270 = models.TextField(db_column='Q270', blank=True, null=True)  # Field name made lowercase.
    q271 = models.TextField(db_column='Q271', blank=True, null=True)  # Field name made lowercase.
    q272 = models.TextField(db_column='Q272', blank=True, null=True)  # Field name made lowercase.
    q273 = models.TextField(db_column='Q273', blank=True, null=True)  # Field name made lowercase.
    q274 = models.TextField(db_column='Q274', blank=True, null=True)  # Field name made lowercase.
    q275 = models.TextField(db_column='Q275', blank=True, null=True)  # Field name made lowercase.
    q275a = models.TextField(db_column='Q275A', blank=True, null=True)  # Field name made lowercase.
    q275r = models.TextField(db_column='Q275R', blank=True, null=True)  # Field name made lowercase.
    q276 = models.TextField(db_column='Q276', blank=True, null=True)  # Field name made lowercase.
    q276a = models.TextField(db_column='Q276A', blank=True, null=True)  # Field name made lowercase.
    q276r = models.TextField(db_column='Q276R', blank=True, null=True)  # Field name made lowercase.
    q277 = models.TextField(db_column='Q277', blank=True, null=True)  # Field name made lowercase.
    q277a = models.TextField(db_column='Q277A', blank=True, null=True)  # Field name made lowercase.
    q277r = models.TextField(db_column='Q277R', blank=True, null=True)  # Field name made lowercase.
    q278 = models.TextField(db_column='Q278', blank=True, null=True)  # Field name made lowercase.
    q278a = models.TextField(db_column='Q278A', blank=True, null=True)  # Field name made lowercase.
    q278r = models.TextField(db_column='Q278R', blank=True, null=True)  # Field name made lowercase.
    q279 = models.TextField(db_column='Q279', blank=True, null=True)  # Field name made lowercase.
    q280 = models.TextField(db_column='Q280', blank=True, null=True)  # Field name made lowercase.
    q281 = models.TextField(db_column='Q281', blank=True, null=True)  # Field name made lowercase.
    q282 = models.TextField(db_column='Q282', blank=True, null=True)  # Field name made lowercase.
    q283 = models.TextField(db_column='Q283', blank=True, null=True)  # Field name made lowercase.
    q284 = models.TextField(db_column='Q284', blank=True, null=True)  # Field name made lowercase.
    q285 = models.TextField(db_column='Q285', blank=True, null=True)  # Field name made lowercase.
    q286 = models.TextField(db_column='Q286', blank=True, null=True)  # Field name made lowercase.
    q287 = models.TextField(db_column='Q287', blank=True, null=True)  # Field name made lowercase.
    q288 = models.TextField(db_column='Q288', blank=True, null=True)  # Field name made lowercase.
    q288r = models.TextField(db_column='Q288R', blank=True, null=True)  # Field name made lowercase.
    q289 = models.TextField(db_column='Q289', blank=True, null=True)  # Field name made lowercase.
    q289cs9 = models.TextField(db_column='Q289CS9', blank=True, null=True)  # Field name made lowercase.
    q290 = models.TextField(db_column='Q290', blank=True, null=True)  # Field name made lowercase.
    y001 = models.TextField(db_column='Y001', blank=True, null=True)  # Field name made lowercase.
    y002 = models.TextField(db_column='Y002', blank=True, null=True)  # Field name made lowercase.
    y003 = models.TextField(db_column='Y003', blank=True, null=True)  # Field name made lowercase.
    sacsecval = models.TextField(db_column='SACSECVAL', blank=True, null=True)  # Field name made lowercase.
    resemaval = models.TextField(db_column='RESEMAVAL', blank=True, null=True)  # Field name made lowercase.
    i_authority = models.TextField(db_column='I_AUTHORITY', blank=True, null=True)  # Field name made lowercase.
    i_nationalism = models.TextField(db_column='I_NATIONALISM', blank=True, null=True)  # Field name made lowercase.
    i_devout = models.TextField(db_column='I_DEVOUT', blank=True, null=True)  # Field name made lowercase.
    defiance = models.TextField(db_column='DEFIANCE', blank=True, null=True)  # Field name made lowercase.
    i_religimp = models.TextField(db_column='I_RELIGIMP', blank=True, null=True)  # Field name made lowercase.
    i_religbel = models.TextField(db_column='I_RELIGBEL', blank=True, null=True)  # Field name made lowercase.
    i_religprac = models.TextField(db_column='I_RELIGPRAC', blank=True, null=True)  # Field name made lowercase.
    disbelief = models.TextField(db_column='DISBELIEF', blank=True, null=True)  # Field name made lowercase.
    i_norm1 = models.TextField(db_column='I_NORM1', blank=True, null=True)  # Field name made lowercase.
    i_norm2 = models.TextField(db_column='I_NORM2', blank=True, null=True)  # Field name made lowercase.
    i_norm3 = models.TextField(db_column='I_NORM3', blank=True, null=True)  # Field name made lowercase.
    relativism = models.TextField(db_column='RELATIVISM', blank=True, null=True)  # Field name made lowercase.
    i_trustarmy = models.TextField(db_column='I_TRUSTARMY', blank=True, null=True)  # Field name made lowercase.
    i_trustpolice = models.TextField(db_column='I_TRUSTPOLICE', blank=True, null=True)  # Field name made lowercase.
    i_trustcourts = models.TextField(db_column='I_TRUSTCOURTS', blank=True, null=True)  # Field name made lowercase.
    scepticism = models.TextField(db_column='SCEPTICISM', blank=True, null=True)  # Field name made lowercase.
    i_indep = models.TextField(db_column='I_INDEP', blank=True, null=True)  # Field name made lowercase.
    i_imagin = models.TextField(db_column='I_IMAGIN', blank=True, null=True)  # Field name made lowercase.
    i_nonobed = models.TextField(db_column='I_NONOBED', blank=True, null=True)  # Field name made lowercase.
    autonomy = models.TextField(db_column='AUTONOMY', blank=True, null=True)  # Field name made lowercase.
    i_womjob = models.TextField(db_column='I_WOMJOB', blank=True, null=True)  # Field name made lowercase.
    i_wompol = models.TextField(db_column='I_WOMPOL', blank=True, null=True)  # Field name made lowercase.
    i_womedu = models.TextField(db_column='I_WOMEDU', blank=True, null=True)  # Field name made lowercase.
    equality = models.TextField(db_column='EQUALITY', blank=True, null=True)  # Field name made lowercase.
    i_homolib = models.TextField(db_column='I_HOMOLIB', blank=True, null=True)  # Field name made lowercase.
    i_abortlib = models.TextField(db_column='I_ABORTLIB', blank=True, null=True)  # Field name made lowercase.
    i_divorlib = models.TextField(db_column='I_DIVORLIB', blank=True, null=True)  # Field name made lowercase.
    choice = models.TextField(db_column='CHOICE', blank=True, null=True)  # Field name made lowercase.
    i_voice1 = models.TextField(db_column='I_VOICE1', blank=True, null=True)  # Field name made lowercase.
    i_voice2 = models.TextField(db_column='I_VOICE2', blank=True, null=True)  # Field name made lowercase.
    i_voi2_00 = models.TextField(db_column='I_VOI2_00', blank=True, null=True)  # Field name made lowercase.
    voice = models.TextField(db_column='VOICE', blank=True, null=True)  # Field name made lowercase.
    secvalwgt = models.TextField(db_column='SECVALWGT', blank=True, null=True)  # Field name made lowercase.
    resemavalwgt = models.TextField(db_column='RESEMAVALWGT', blank=True, null=True)  # Field name made lowercase.
    fhregion = models.TextField(blank=True, null=True)
    polregfh = models.TextField(blank=True, null=True)
    freestfh = models.TextField(blank=True, null=True)
    prfhrat = models.TextField(blank=True, null=True)
    prfhscore = models.TextField(blank=True, null=True)
    clfhrat = models.TextField(blank=True, null=True)
    clfhscore = models.TextField(blank=True, null=True)
    democ = models.TextField(blank=True, null=True)
    autoc = models.TextField(blank=True, null=True)
    polity = models.TextField(blank=True, null=True)
    durable = models.TextField(blank=True, null=True)
    regtype = models.TextField(blank=True, null=True)
    ruleoflaw = models.TextField(blank=True, null=True)
    corrupttransp = models.TextField(blank=True, null=True)
    electintegr = models.TextField(blank=True, null=True)
    btiregion = models.TextField(blank=True, null=True)
    btistatus = models.TextField(blank=True, null=True)
    btidemstatus = models.TextField(blank=True, null=True)
    btistate = models.TextField(blank=True, null=True)
    btipolpart = models.TextField(blank=True, null=True)
    btiruleoflaw = models.TextField(blank=True, null=True)
    btistability = models.TextField(blank=True, null=True)
    btiintegration = models.TextField(blank=True, null=True)
    btimarket = models.TextField(blank=True, null=True)
    btigovindex = models.TextField(blank=True, null=True)
    btigoveperform = models.TextField(blank=True, null=True)
    btiregime = models.TextField(blank=True, null=True)
    regionwb = models.TextField(db_column='regionWB', blank=True, null=True)  # Field name made lowercase.
    incomewb = models.TextField(db_column='incomeWB', blank=True, null=True)  # Field name made lowercase.
    landwb = models.TextField(db_column='landWB', blank=True, null=True)  # Field name made lowercase.
    gdppercap1 = models.TextField(db_column='GDPpercap1', blank=True, null=True)  # Field name made lowercase.
    gdppercap2 = models.TextField(db_column='GDPpercap2', blank=True, null=True)  # Field name made lowercase.
    giniwb = models.TextField(db_column='giniWB', blank=True, null=True)  # Field name made lowercase.
    incrichest10p = models.TextField(blank=True, null=True)
    popwb1990 = models.TextField(db_column='popWB1990', blank=True, null=True)  # Field name made lowercase.
    popwb2000 = models.TextField(db_column='popWB2000', blank=True, null=True)  # Field name made lowercase.
    popwb2019 = models.TextField(db_column='popWB2019', blank=True, null=True)  # Field name made lowercase.
    lifeexpect = models.TextField(blank=True, null=True)
    popgrowth = models.TextField(blank=True, null=True)
    urbanpop = models.TextField(blank=True, null=True)
    laborforce = models.TextField(blank=True, null=True)
    deathrate = models.TextField(blank=True, null=True)
    unemployfem = models.TextField(blank=True, null=True)
    unemploymale = models.TextField(blank=True, null=True)
    unemploytotal = models.TextField(blank=True, null=True)
    accessclfuel = models.TextField(blank=True, null=True)
    accesselectr = models.TextField(blank=True, null=True)
    renewelectr = models.TextField(blank=True, null=True)
    co2emis = models.TextField(blank=True, null=True)
    co2percap = models.TextField(blank=True, null=True)
    easeofbusiness = models.TextField(blank=True, null=True)
    militaryexp = models.TextField(blank=True, null=True)
    trade = models.TextField(db_column='Trade', blank=True, null=True)  # Field name made lowercase.
    healthexp = models.TextField(blank=True, null=True)
    educationexp = models.TextField(blank=True, null=True)
    medageun = models.TextField(blank=True, null=True)
    meanschooling = models.TextField(blank=True, null=True)
    educationhdi = models.TextField(db_column='educationHDI', blank=True, null=True)  # Field name made lowercase.
    compulseduc = models.TextField(blank=True, null=True)
    gii = models.TextField(db_column='GII', blank=True, null=True)  # Field name made lowercase.
    dgi = models.TextField(db_column='DGI', blank=True, null=True)  # Field name made lowercase.
    womenparl = models.TextField(blank=True, null=True)
    hdi = models.TextField(blank=True, null=True)
    incomeindexhdi = models.TextField(db_column='incomeindexHDI', blank=True, null=True)  # Field name made lowercase.
    humanineqiality = models.TextField(blank=True, null=True)
    lifeexpecthdi = models.TextField(db_column='lifeexpectHDI', blank=True, null=True)  # Field name made lowercase.
    homiciderate = models.TextField(blank=True, null=True)
    refugeesorigin = models.TextField(db_column='Refugeesorigin', blank=True, null=True)  # Field name made lowercase.
    internetusers = models.TextField(blank=True, null=True)
    mobphone = models.TextField(blank=True, null=True)
    migrationrate = models.TextField(blank=True, null=True)
    schoolgpi = models.TextField(blank=True, null=True)
    femchoutsch = models.TextField(blank=True, null=True)
    choutsch = models.TextField(blank=True, null=True)
    v2x_polyarchy = models.TextField(blank=True, null=True)
    v2x_libdem = models.TextField(blank=True, null=True)
    v2x_partipdem = models.TextField(blank=True, null=True)
    v2x_delibdem = models.TextField(blank=True, null=True)
    v2x_egaldem = models.TextField(blank=True, null=True)
    v2x_freexp_altinf = models.TextField(blank=True, null=True)
    v2x_frassoc_thick = models.TextField(blank=True, null=True)
    v2xel_frefair = models.TextField(blank=True, null=True)
    v2xcl_rol = models.TextField(blank=True, null=True)
    v2x_cspart = models.TextField(blank=True, null=True)
    v2xeg_eqdr = models.TextField(blank=True, null=True)
    v2excrptps = models.TextField(blank=True, null=True)
    v2exthftps = models.TextField(blank=True, null=True)
    v2juaccnt = models.TextField(blank=True, null=True)
    v2cltrnslw = models.TextField(blank=True, null=True)
    v2clacjust = models.TextField(blank=True, null=True)
    v2clsocgrp = models.TextField(blank=True, null=True)
    v2clacfree = models.TextField(blank=True, null=True)
    v2clrelig = models.TextField(blank=True, null=True)
    v2csrlgrep = models.TextField(blank=True, null=True)
    v2mecenefm = models.TextField(blank=True, null=True)
    v2mecenefi = models.TextField(blank=True, null=True)
    v2mebias = models.TextField(blank=True, null=True)
    v2pepwrses = models.TextField(blank=True, null=True)
    v2pepwrgen = models.TextField(blank=True, null=True)
    v2peedueq = models.TextField(blank=True, null=True)
    v2pehealth = models.TextField(blank=True, null=True)
    v2peapsecon = models.TextField(blank=True, null=True)
    v2peasjsoecon = models.TextField(blank=True, null=True)
    v2clgencl = models.TextField(blank=True, null=True)
    v2peasjgen = models.TextField(blank=True, null=True)
    v2peasbgen = models.TextField(blank=True, null=True)
    v2cafres = models.TextField(blank=True, null=True)
    v2cafexch = models.TextField(blank=True, null=True)
    v2x_corr = models.TextField(blank=True, null=True)
    v2x_gender = models.TextField(blank=True, null=True)
    v2x_gencl = models.TextField(blank=True, null=True)
    v2x_genpp = models.TextField(blank=True, null=True)
    v2x_rule = models.TextField(blank=True, null=True)
    v2xcl_acjst = models.TextField(blank=True, null=True)
    id_gps = models.TextField(db_column='ID_GPS', blank=True, null=True)  # Field name made lowercase.
    id_partyfacts = models.TextField(db_column='ID_PartyFacts', blank=True, null=True)  # Field name made lowercase.
    partyname = models.TextField(db_column='Partyname', blank=True, null=True)  # Field name made lowercase.
    partyabb = models.TextField(db_column='Partyabb', blank=True, null=True)  # Field name made lowercase.
    cparty = models.TextField(db_column='CPARTY', blank=True, null=True)  # Field name made lowercase.
    cpartyabb = models.TextField(db_column='CPARTYABB', blank=True, null=True)  # Field name made lowercase.
    type_values = models.TextField(db_column='Type_Values', blank=True, null=True)  # Field name made lowercase.
    type_populism = models.TextField(db_column='Type_Populism', blank=True, null=True)  # Field name made lowercase.
    type_populist_values = models.TextField(db_column='Type_Populist_Values', blank=True, null=True)  # Field name made lowercase.
    type_partysize_vote = models.TextField(db_column='Type_Partysize_vote', blank=True, null=True)  # Field name made lowercase.
    type_partysize_seat = models.TextField(db_column='Type_Partysize_seat', blank=True, null=True)  # Field name made lowercase.
    gps_v4_scale = models.TextField(db_column='GPS_V4_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v6_scale = models.TextField(db_column='GPS_V6_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v8_scale = models.TextField(db_column='GPS_V8_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v9 = models.TextField(db_column='GPS_V9', blank=True, null=True)  # Field name made lowercase.
    gps_v10 = models.TextField(db_column='GPS_V10', blank=True, null=True)  # Field name made lowercase.
    gps_v11 = models.TextField(db_column='GPS_V11', blank=True, null=True)  # Field name made lowercase.
    gps_v12 = models.TextField(db_column='GPS_V12', blank=True, null=True)  # Field name made lowercase.
    gps_v13 = models.TextField(db_column='GPS_V13', blank=True, null=True)  # Field name made lowercase.
    gps_v14 = models.TextField(db_column='GPS_V14', blank=True, null=True)  # Field name made lowercase.
    gps_v15 = models.TextField(db_column='GPS_V15', blank=True, null=True)  # Field name made lowercase.
    gps_v16 = models.TextField(db_column='GPS_V16', blank=True, null=True)  # Field name made lowercase.
    gps_v17 = models.TextField(db_column='GPS_V17', blank=True, null=True)  # Field name made lowercase.
    wvs_lr_partyvoter = models.TextField(db_column='WVS_LR_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_libcon_partyvoter = models.TextField(db_column='WVS_LibCon_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_polmistrust_partyvoter = models.TextField(db_column='WVS_Polmistrust_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_lr_medianvoter = models.TextField(db_column='WVS_LR_MedianVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_libcon_medianvoter = models.TextField(db_column='WVS_LibCon_MedianVoter', blank=True, null=True)  # Field name made lowercase.
    v2psbars = models.TextField(blank=True, null=True)
    v2psorgs = models.TextField(blank=True, null=True)
    v2psprbrch = models.TextField(blank=True, null=True)
    v2psprlnks = models.TextField(blank=True, null=True)
    v2psplats = models.TextField(blank=True, null=True)
    v2xnp_client = models.TextField(blank=True, null=True)
    v2xps_party = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuestionsLarge(models.Model):
    version = models.TextField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    a_wave = models.TextField(db_column='A_WAVE', blank=True, null=True)  # Field name made lowercase.
    a_study = models.TextField(db_column='A_STUDY', blank=True, null=True)  # Field name made lowercase.
    b_country = models.TextField(db_column='B_COUNTRY', blank=True, null=True)  # Field name made lowercase.
    b_country_alpha = models.TextField(db_column='B_COUNTRY_ALPHA', blank=True, null=True)  # Field name made lowercase.
    c_cow_num = models.TextField(db_column='C_COW_NUM', blank=True, null=True)  # Field name made lowercase.
    c_cow_alpha = models.TextField(db_column='C_COW_ALPHA', blank=True, null=True)  # Field name made lowercase.
    a_year = models.TextField(db_column='A_YEAR', blank=True, null=True)  # Field name made lowercase.
    d_interview = models.TextField(db_column='D_INTERVIEW', blank=True, null=True)  # Field name made lowercase.
    j_intdate = models.TextField(db_column='J_INTDATE', blank=True, null=True)  # Field name made lowercase.
    fw_end = models.TextField(db_column='FW_END', blank=True, null=True)  # Field name made lowercase.
    fw_start = models.TextField(db_column='FW_START', blank=True, null=True)  # Field name made lowercase.
    k_time_start = models.TextField(db_column='K_TIME_START', blank=True, null=True)  # Field name made lowercase.
    k_time_end = models.TextField(db_column='K_TIME_END', blank=True, null=True)  # Field name made lowercase.
    k_duration = models.TextField(db_column='K_DURATION', blank=True, null=True)  # Field name made lowercase.
    q_mode = models.TextField(db_column='Q_MODE', blank=True, null=True)  # Field name made lowercase.
    n_region_iso = models.TextField(db_column='N_REGION_ISO', blank=True, null=True)  # Field name made lowercase.
    n_region_wvs = models.TextField(db_column='N_REGION_WVS', blank=True, null=True)  # Field name made lowercase.
    n_town = models.TextField(db_column='N_TOWN', blank=True, null=True)  # Field name made lowercase.
    g_townsize = models.TextField(db_column='G_TOWNSIZE', blank=True, null=True)  # Field name made lowercase.
    g_townsize2 = models.TextField(db_column='G_TOWNSIZE2', blank=True, null=True)  # Field name made lowercase.
    h_settlement = models.TextField(db_column='H_SETTLEMENT', blank=True, null=True)  # Field name made lowercase.
    h_urbrural = models.TextField(db_column='H_URBRURAL', blank=True, null=True)  # Field name made lowercase.
    i_psu = models.TextField(db_column='I_PSU', blank=True, null=True)  # Field name made lowercase.
    o1_longitude = models.TextField(db_column='O1_LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    o2_latitude = models.TextField(db_column='O2_LATITUDE', blank=True, null=True)  # Field name made lowercase.
    s_intlanguage = models.TextField(db_column='S_INTLANGUAGE', blank=True, null=True)  # Field name made lowercase.
    lnge_iso = models.TextField(db_column='LNGE_ISO', blank=True, null=True)  # Field name made lowercase.
    e_respint = models.TextField(db_column='E_RESPINT', blank=True, null=True)  # Field name made lowercase.
    f_intprivacy = models.TextField(db_column='F_INTPRIVACY', blank=True, null=True)  # Field name made lowercase.
    e1_literacy = models.TextField(db_column='E1_LITERACY', blank=True, null=True)  # Field name made lowercase.
    w_weight = models.TextField(db_column='W_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    s018 = models.TextField(db_column='S018', blank=True, null=True)  # Field name made lowercase.
    pwght = models.TextField(db_column='PWGHT', blank=True, null=True)  # Field name made lowercase.
    s025 = models.TextField(db_column='S025', blank=True, null=True)  # Field name made lowercase.
    q1 = models.TextField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.TextField(db_column='Q2', blank=True, null=True)  # Field name made lowercase.
    q3 = models.TextField(db_column='Q3', blank=True, null=True)  # Field name made lowercase.
    q4 = models.TextField(db_column='Q4', blank=True, null=True)  # Field name made lowercase.
    q5 = models.TextField(db_column='Q5', blank=True, null=True)  # Field name made lowercase.
    q6 = models.TextField(db_column='Q6', blank=True, null=True)  # Field name made lowercase.
    q7 = models.TextField(db_column='Q7', blank=True, null=True)  # Field name made lowercase.
    q8 = models.TextField(db_column='Q8', blank=True, null=True)  # Field name made lowercase.
    q9 = models.TextField(db_column='Q9', blank=True, null=True)  # Field name made lowercase.
    q10 = models.TextField(db_column='Q10', blank=True, null=True)  # Field name made lowercase.
    q11 = models.TextField(db_column='Q11', blank=True, null=True)  # Field name made lowercase.
    q12 = models.TextField(db_column='Q12', blank=True, null=True)  # Field name made lowercase.
    q13 = models.TextField(db_column='Q13', blank=True, null=True)  # Field name made lowercase.
    q14 = models.TextField(db_column='Q14', blank=True, null=True)  # Field name made lowercase.
    q15 = models.TextField(db_column='Q15', blank=True, null=True)  # Field name made lowercase.
    q16 = models.TextField(db_column='Q16', blank=True, null=True)  # Field name made lowercase.
    q17 = models.TextField(db_column='Q17', blank=True, null=True)  # Field name made lowercase.
    q18 = models.TextField(db_column='Q18', blank=True, null=True)  # Field name made lowercase.
    q19 = models.TextField(db_column='Q19', blank=True, null=True)  # Field name made lowercase.
    q20 = models.TextField(db_column='Q20', blank=True, null=True)  # Field name made lowercase.
    q21 = models.TextField(db_column='Q21', blank=True, null=True)  # Field name made lowercase.
    q22 = models.TextField(db_column='Q22', blank=True, null=True)  # Field name made lowercase.
    q23 = models.TextField(db_column='Q23', blank=True, null=True)  # Field name made lowercase.
    q24 = models.TextField(db_column='Q24', blank=True, null=True)  # Field name made lowercase.
    q25 = models.TextField(db_column='Q25', blank=True, null=True)  # Field name made lowercase.
    q26 = models.TextField(db_column='Q26', blank=True, null=True)  # Field name made lowercase.
    q27 = models.TextField(db_column='Q27', blank=True, null=True)  # Field name made lowercase.
    q28 = models.TextField(db_column='Q28', blank=True, null=True)  # Field name made lowercase.
    q29 = models.TextField(db_column='Q29', blank=True, null=True)  # Field name made lowercase.
    q30 = models.TextField(db_column='Q30', blank=True, null=True)  # Field name made lowercase.
    q31 = models.TextField(db_column='Q31', blank=True, null=True)  # Field name made lowercase.
    q32 = models.TextField(db_column='Q32', blank=True, null=True)  # Field name made lowercase.
    q33 = models.TextField(db_column='Q33', blank=True, null=True)  # Field name made lowercase.
    q33_3 = models.TextField(db_column='Q33_3', blank=True, null=True)  # Field name made lowercase.
    q34 = models.TextField(db_column='Q34', blank=True, null=True)  # Field name made lowercase.
    q34_3 = models.TextField(db_column='Q34_3', blank=True, null=True)  # Field name made lowercase.
    q35 = models.TextField(db_column='Q35', blank=True, null=True)  # Field name made lowercase.
    q35_3 = models.TextField(db_column='Q35_3', blank=True, null=True)  # Field name made lowercase.
    q36 = models.TextField(db_column='Q36', blank=True, null=True)  # Field name made lowercase.
    q37 = models.TextField(db_column='Q37', blank=True, null=True)  # Field name made lowercase.
    q38 = models.TextField(db_column='Q38', blank=True, null=True)  # Field name made lowercase.
    q39 = models.TextField(db_column='Q39', blank=True, null=True)  # Field name made lowercase.
    q40 = models.TextField(db_column='Q40', blank=True, null=True)  # Field name made lowercase.
    q41 = models.TextField(db_column='Q41', blank=True, null=True)  # Field name made lowercase.
    q42 = models.TextField(db_column='Q42', blank=True, null=True)  # Field name made lowercase.
    q43 = models.TextField(db_column='Q43', blank=True, null=True)  # Field name made lowercase.
    q44 = models.TextField(db_column='Q44', blank=True, null=True)  # Field name made lowercase.
    q45 = models.TextField(db_column='Q45', blank=True, null=True)  # Field name made lowercase.
    q46 = models.TextField(db_column='Q46', blank=True, null=True)  # Field name made lowercase.
    q47 = models.TextField(db_column='Q47', blank=True, null=True)  # Field name made lowercase.
    q48 = models.TextField(db_column='Q48', blank=True, null=True)  # Field name made lowercase.
    q49 = models.TextField(db_column='Q49', blank=True, null=True)  # Field name made lowercase.
    q50 = models.TextField(db_column='Q50', blank=True, null=True)  # Field name made lowercase.
    q51 = models.TextField(db_column='Q51', blank=True, null=True)  # Field name made lowercase.
    q52 = models.TextField(db_column='Q52', blank=True, null=True)  # Field name made lowercase.
    q53 = models.TextField(db_column='Q53', blank=True, null=True)  # Field name made lowercase.
    q54 = models.TextField(db_column='Q54', blank=True, null=True)  # Field name made lowercase.
    q55 = models.TextField(db_column='Q55', blank=True, null=True)  # Field name made lowercase.
    q56 = models.TextField(db_column='Q56', blank=True, null=True)  # Field name made lowercase.
    q57 = models.TextField(db_column='Q57', blank=True, null=True)  # Field name made lowercase.
    q58 = models.TextField(db_column='Q58', blank=True, null=True)  # Field name made lowercase.
    q59 = models.TextField(db_column='Q59', blank=True, null=True)  # Field name made lowercase.
    q60 = models.TextField(db_column='Q60', blank=True, null=True)  # Field name made lowercase.
    q61 = models.TextField(db_column='Q61', blank=True, null=True)  # Field name made lowercase.
    q62 = models.TextField(db_column='Q62', blank=True, null=True)  # Field name made lowercase.
    q63 = models.TextField(db_column='Q63', blank=True, null=True)  # Field name made lowercase.
    q64 = models.TextField(db_column='Q64', blank=True, null=True)  # Field name made lowercase.
    q65 = models.TextField(db_column='Q65', blank=True, null=True)  # Field name made lowercase.
    q66 = models.TextField(db_column='Q66', blank=True, null=True)  # Field name made lowercase.
    q67 = models.TextField(db_column='Q67', blank=True, null=True)  # Field name made lowercase.
    q68 = models.TextField(db_column='Q68', blank=True, null=True)  # Field name made lowercase.
    q69 = models.TextField(db_column='Q69', blank=True, null=True)  # Field name made lowercase.
    q70 = models.TextField(db_column='Q70', blank=True, null=True)  # Field name made lowercase.
    q71 = models.TextField(db_column='Q71', blank=True, null=True)  # Field name made lowercase.
    q72 = models.TextField(db_column='Q72', blank=True, null=True)  # Field name made lowercase.
    q73 = models.TextField(db_column='Q73', blank=True, null=True)  # Field name made lowercase.
    q74 = models.TextField(db_column='Q74', blank=True, null=True)  # Field name made lowercase.
    q75 = models.TextField(db_column='Q75', blank=True, null=True)  # Field name made lowercase.
    q76 = models.TextField(db_column='Q76', blank=True, null=True)  # Field name made lowercase.
    q77 = models.TextField(db_column='Q77', blank=True, null=True)  # Field name made lowercase.
    q78 = models.TextField(db_column='Q78', blank=True, null=True)  # Field name made lowercase.
    q79 = models.TextField(db_column='Q79', blank=True, null=True)  # Field name made lowercase.
    q80 = models.TextField(db_column='Q80', blank=True, null=True)  # Field name made lowercase.
    q81 = models.TextField(db_column='Q81', blank=True, null=True)  # Field name made lowercase.
    q82 = models.TextField(db_column='Q82', blank=True, null=True)  # Field name made lowercase.
    q82_eu = models.TextField(db_column='Q82_EU', blank=True, null=True)  # Field name made lowercase.
    q82_apec = models.TextField(db_column='Q82_APEC', blank=True, null=True)  # Field name made lowercase.
    q82_arableague = models.TextField(db_column='Q82_ARABLEAGUE', blank=True, null=True)  # Field name made lowercase.
    q82_asean = models.TextField(db_column='Q82_ASEAN', blank=True, null=True)  # Field name made lowercase.
    q82_africanunion = models.TextField(db_column='Q82_AFRICANUNION', blank=True, null=True)  # Field name made lowercase.
    q82_cis = models.TextField(db_column='Q82_CIS', blank=True, null=True)  # Field name made lowercase.
    q82_eco = models.TextField(db_column='Q82_ECO', blank=True, null=True)  # Field name made lowercase.
    q82_gulfcoop = models.TextField(db_column='Q82_GULFCOOP', blank=True, null=True)  # Field name made lowercase.
    q82_islcoop = models.TextField(db_column='Q82_ISLCOOP', blank=True, null=True)  # Field name made lowercase.
    q82_mercosur = models.TextField(db_column='Q82_MERCOSUR', blank=True, null=True)  # Field name made lowercase.
    q82_nafta = models.TextField(db_column='Q82_NAFTA', blank=True, null=True)  # Field name made lowercase.
    q82_oas = models.TextField(db_column='Q82_OAS', blank=True, null=True)  # Field name made lowercase.
    q82_saarc = models.TextField(db_column='Q82_SAARC', blank=True, null=True)  # Field name made lowercase.
    q82_sco = models.TextField(db_column='Q82_SCO', blank=True, null=True)  # Field name made lowercase.
    q82_tlc = models.TextField(db_column='Q82_TLC', blank=True, null=True)  # Field name made lowercase.
    q82_undp = models.TextField(db_column='Q82_UNDP', blank=True, null=True)  # Field name made lowercase.
    q83 = models.TextField(db_column='Q83', blank=True, null=True)  # Field name made lowercase.
    q84 = models.TextField(db_column='Q84', blank=True, null=True)  # Field name made lowercase.
    q85 = models.TextField(db_column='Q85', blank=True, null=True)  # Field name made lowercase.
    q86 = models.TextField(db_column='Q86', blank=True, null=True)  # Field name made lowercase.
    q87 = models.TextField(db_column='Q87', blank=True, null=True)  # Field name made lowercase.
    q88 = models.TextField(db_column='Q88', blank=True, null=True)  # Field name made lowercase.
    q89 = models.TextField(db_column='Q89', blank=True, null=True)  # Field name made lowercase.
    q90 = models.TextField(db_column='Q90', blank=True, null=True)  # Field name made lowercase.
    q91 = models.TextField(db_column='Q91', blank=True, null=True)  # Field name made lowercase.
    q92 = models.TextField(db_column='Q92', blank=True, null=True)  # Field name made lowercase.
    q93 = models.TextField(db_column='Q93', blank=True, null=True)  # Field name made lowercase.
    q94 = models.TextField(db_column='Q94', blank=True, null=True)  # Field name made lowercase.
    q95 = models.TextField(db_column='Q95', blank=True, null=True)  # Field name made lowercase.
    q96 = models.TextField(db_column='Q96', blank=True, null=True)  # Field name made lowercase.
    q97 = models.TextField(db_column='Q97', blank=True, null=True)  # Field name made lowercase.
    q98 = models.TextField(db_column='Q98', blank=True, null=True)  # Field name made lowercase.
    q99 = models.TextField(db_column='Q99', blank=True, null=True)  # Field name made lowercase.
    q100 = models.TextField(db_column='Q100', blank=True, null=True)  # Field name made lowercase.
    q101 = models.TextField(db_column='Q101', blank=True, null=True)  # Field name made lowercase.
    q102 = models.TextField(db_column='Q102', blank=True, null=True)  # Field name made lowercase.
    q103 = models.TextField(db_column='Q103', blank=True, null=True)  # Field name made lowercase.
    q104 = models.TextField(db_column='Q104', blank=True, null=True)  # Field name made lowercase.
    q105 = models.TextField(db_column='Q105', blank=True, null=True)  # Field name made lowercase.
    q106 = models.TextField(db_column='Q106', blank=True, null=True)  # Field name made lowercase.
    q107 = models.TextField(db_column='Q107', blank=True, null=True)  # Field name made lowercase.
    q108 = models.TextField(db_column='Q108', blank=True, null=True)  # Field name made lowercase.
    q109 = models.TextField(db_column='Q109', blank=True, null=True)  # Field name made lowercase.
    q110 = models.TextField(db_column='Q110', blank=True, null=True)  # Field name made lowercase.
    q111 = models.TextField(db_column='Q111', blank=True, null=True)  # Field name made lowercase.
    q112 = models.TextField(db_column='Q112', blank=True, null=True)  # Field name made lowercase.
    q113 = models.TextField(db_column='Q113', blank=True, null=True)  # Field name made lowercase.
    q114 = models.TextField(db_column='Q114', blank=True, null=True)  # Field name made lowercase.
    q115 = models.TextField(db_column='Q115', blank=True, null=True)  # Field name made lowercase.
    q116 = models.TextField(db_column='Q116', blank=True, null=True)  # Field name made lowercase.
    q117 = models.TextField(db_column='Q117', blank=True, null=True)  # Field name made lowercase.
    q118 = models.TextField(db_column='Q118', blank=True, null=True)  # Field name made lowercase.
    q119 = models.TextField(db_column='Q119', blank=True, null=True)  # Field name made lowercase.
    q120 = models.TextField(db_column='Q120', blank=True, null=True)  # Field name made lowercase.
    q121 = models.TextField(db_column='Q121', blank=True, null=True)  # Field name made lowercase.
    q122 = models.TextField(db_column='Q122', blank=True, null=True)  # Field name made lowercase.
    q123 = models.TextField(db_column='Q123', blank=True, null=True)  # Field name made lowercase.
    q124 = models.TextField(db_column='Q124', blank=True, null=True)  # Field name made lowercase.
    q125 = models.TextField(db_column='Q125', blank=True, null=True)  # Field name made lowercase.
    q126 = models.TextField(db_column='Q126', blank=True, null=True)  # Field name made lowercase.
    q127 = models.TextField(db_column='Q127', blank=True, null=True)  # Field name made lowercase.
    q128 = models.TextField(db_column='Q128', blank=True, null=True)  # Field name made lowercase.
    q129 = models.TextField(db_column='Q129', blank=True, null=True)  # Field name made lowercase.
    q130 = models.TextField(db_column='Q130', blank=True, null=True)  # Field name made lowercase.
    q131 = models.TextField(db_column='Q131', blank=True, null=True)  # Field name made lowercase.
    q132 = models.TextField(db_column='Q132', blank=True, null=True)  # Field name made lowercase.
    q133 = models.TextField(db_column='Q133', blank=True, null=True)  # Field name made lowercase.
    q134 = models.TextField(db_column='Q134', blank=True, null=True)  # Field name made lowercase.
    q135 = models.TextField(db_column='Q135', blank=True, null=True)  # Field name made lowercase.
    q136 = models.TextField(db_column='Q136', blank=True, null=True)  # Field name made lowercase.
    q137 = models.TextField(db_column='Q137', blank=True, null=True)  # Field name made lowercase.
    q138 = models.TextField(db_column='Q138', blank=True, null=True)  # Field name made lowercase.
    q139 = models.TextField(db_column='Q139', blank=True, null=True)  # Field name made lowercase.
    q140 = models.TextField(db_column='Q140', blank=True, null=True)  # Field name made lowercase.
    q141 = models.TextField(db_column='Q141', blank=True, null=True)  # Field name made lowercase.
    q142 = models.TextField(db_column='Q142', blank=True, null=True)  # Field name made lowercase.
    q143 = models.TextField(db_column='Q143', blank=True, null=True)  # Field name made lowercase.
    q144 = models.TextField(db_column='Q144', blank=True, null=True)  # Field name made lowercase.
    q145 = models.TextField(db_column='Q145', blank=True, null=True)  # Field name made lowercase.
    q146 = models.TextField(db_column='Q146', blank=True, null=True)  # Field name made lowercase.
    q147 = models.TextField(db_column='Q147', blank=True, null=True)  # Field name made lowercase.
    q148 = models.TextField(db_column='Q148', blank=True, null=True)  # Field name made lowercase.
    q149 = models.TextField(db_column='Q149', blank=True, null=True)  # Field name made lowercase.
    q150 = models.TextField(db_column='Q150', blank=True, null=True)  # Field name made lowercase.
    q151 = models.TextField(db_column='Q151', blank=True, null=True)  # Field name made lowercase.
    q152 = models.TextField(db_column='Q152', blank=True, null=True)  # Field name made lowercase.
    q153 = models.TextField(db_column='Q153', blank=True, null=True)  # Field name made lowercase.
    q154 = models.TextField(db_column='Q154', blank=True, null=True)  # Field name made lowercase.
    q155 = models.TextField(db_column='Q155', blank=True, null=True)  # Field name made lowercase.
    q156 = models.TextField(db_column='Q156', blank=True, null=True)  # Field name made lowercase.
    q157 = models.TextField(db_column='Q157', blank=True, null=True)  # Field name made lowercase.
    q158 = models.TextField(db_column='Q158', blank=True, null=True)  # Field name made lowercase.
    q159 = models.TextField(db_column='Q159', blank=True, null=True)  # Field name made lowercase.
    q160 = models.TextField(db_column='Q160', blank=True, null=True)  # Field name made lowercase.
    q161 = models.TextField(db_column='Q161', blank=True, null=True)  # Field name made lowercase.
    q162 = models.TextField(db_column='Q162', blank=True, null=True)  # Field name made lowercase.
    q163 = models.TextField(db_column='Q163', blank=True, null=True)  # Field name made lowercase.
    q164 = models.TextField(db_column='Q164', blank=True, null=True)  # Field name made lowercase.
    q165 = models.TextField(db_column='Q165', blank=True, null=True)  # Field name made lowercase.
    q166 = models.TextField(db_column='Q166', blank=True, null=True)  # Field name made lowercase.
    q167 = models.TextField(db_column='Q167', blank=True, null=True)  # Field name made lowercase.
    q168 = models.TextField(db_column='Q168', blank=True, null=True)  # Field name made lowercase.
    q169 = models.TextField(db_column='Q169', blank=True, null=True)  # Field name made lowercase.
    q170 = models.TextField(db_column='Q170', blank=True, null=True)  # Field name made lowercase.
    q171 = models.TextField(db_column='Q171', blank=True, null=True)  # Field name made lowercase.
    q172 = models.TextField(db_column='Q172', blank=True, null=True)  # Field name made lowercase.
    q173 = models.TextField(db_column='Q173', blank=True, null=True)  # Field name made lowercase.
    q174 = models.TextField(db_column='Q174', blank=True, null=True)  # Field name made lowercase.
    q175 = models.TextField(db_column='Q175', blank=True, null=True)  # Field name made lowercase.
    q176 = models.TextField(db_column='Q176', blank=True, null=True)  # Field name made lowercase.
    q177 = models.TextField(db_column='Q177', blank=True, null=True)  # Field name made lowercase.
    q178 = models.TextField(db_column='Q178', blank=True, null=True)  # Field name made lowercase.
    q179 = models.TextField(db_column='Q179', blank=True, null=True)  # Field name made lowercase.
    q180 = models.TextField(db_column='Q180', blank=True, null=True)  # Field name made lowercase.
    q181 = models.TextField(db_column='Q181', blank=True, null=True)  # Field name made lowercase.
    q182 = models.TextField(db_column='Q182', blank=True, null=True)  # Field name made lowercase.
    q183 = models.TextField(db_column='Q183', blank=True, null=True)  # Field name made lowercase.
    q184 = models.TextField(db_column='Q184', blank=True, null=True)  # Field name made lowercase.
    q185 = models.TextField(db_column='Q185', blank=True, null=True)  # Field name made lowercase.
    q186 = models.TextField(db_column='Q186', blank=True, null=True)  # Field name made lowercase.
    q187 = models.TextField(db_column='Q187', blank=True, null=True)  # Field name made lowercase.
    q188 = models.TextField(db_column='Q188', blank=True, null=True)  # Field name made lowercase.
    q189 = models.TextField(db_column='Q189', blank=True, null=True)  # Field name made lowercase.
    q190 = models.TextField(db_column='Q190', blank=True, null=True)  # Field name made lowercase.
    q191 = models.TextField(db_column='Q191', blank=True, null=True)  # Field name made lowercase.
    q192 = models.TextField(db_column='Q192', blank=True, null=True)  # Field name made lowercase.
    q193 = models.TextField(db_column='Q193', blank=True, null=True)  # Field name made lowercase.
    q194 = models.TextField(db_column='Q194', blank=True, null=True)  # Field name made lowercase.
    q195 = models.TextField(db_column='Q195', blank=True, null=True)  # Field name made lowercase.
    q196 = models.TextField(db_column='Q196', blank=True, null=True)  # Field name made lowercase.
    q197 = models.TextField(db_column='Q197', blank=True, null=True)  # Field name made lowercase.
    q198 = models.TextField(db_column='Q198', blank=True, null=True)  # Field name made lowercase.
    q199 = models.TextField(db_column='Q199', blank=True, null=True)  # Field name made lowercase.
    q200 = models.TextField(db_column='Q200', blank=True, null=True)  # Field name made lowercase.
    q201 = models.TextField(db_column='Q201', blank=True, null=True)  # Field name made lowercase.
    q202 = models.TextField(db_column='Q202', blank=True, null=True)  # Field name made lowercase.
    q203 = models.TextField(db_column='Q203', blank=True, null=True)  # Field name made lowercase.
    q204 = models.TextField(db_column='Q204', blank=True, null=True)  # Field name made lowercase.
    q205 = models.TextField(db_column='Q205', blank=True, null=True)  # Field name made lowercase.
    q206 = models.TextField(db_column='Q206', blank=True, null=True)  # Field name made lowercase.
    q207 = models.TextField(db_column='Q207', blank=True, null=True)  # Field name made lowercase.
    q208 = models.TextField(db_column='Q208', blank=True, null=True)  # Field name made lowercase.
    q209 = models.TextField(db_column='Q209', blank=True, null=True)  # Field name made lowercase.
    q210 = models.TextField(db_column='Q210', blank=True, null=True)  # Field name made lowercase.
    q211 = models.TextField(db_column='Q211', blank=True, null=True)  # Field name made lowercase.
    q212 = models.TextField(db_column='Q212', blank=True, null=True)  # Field name made lowercase.
    q213 = models.TextField(db_column='Q213', blank=True, null=True)  # Field name made lowercase.
    q214 = models.TextField(db_column='Q214', blank=True, null=True)  # Field name made lowercase.
    q215 = models.TextField(db_column='Q215', blank=True, null=True)  # Field name made lowercase.
    q216 = models.TextField(db_column='Q216', blank=True, null=True)  # Field name made lowercase.
    q217 = models.TextField(db_column='Q217', blank=True, null=True)  # Field name made lowercase.
    q218 = models.TextField(db_column='Q218', blank=True, null=True)  # Field name made lowercase.
    q219 = models.TextField(db_column='Q219', blank=True, null=True)  # Field name made lowercase.
    q220 = models.TextField(db_column='Q220', blank=True, null=True)  # Field name made lowercase.
    q221 = models.TextField(db_column='Q221', blank=True, null=True)  # Field name made lowercase.
    q222 = models.TextField(db_column='Q222', blank=True, null=True)  # Field name made lowercase.
    q223 = models.TextField(db_column='Q223', blank=True, null=True)  # Field name made lowercase.
    q223_abrev = models.TextField(db_column='Q223_ABREV', blank=True, null=True)  # Field name made lowercase.
    q223_local = models.TextField(db_column='Q223_LOCAL', blank=True, null=True)  # Field name made lowercase.
    q224 = models.TextField(db_column='Q224', blank=True, null=True)  # Field name made lowercase.
    q225 = models.TextField(db_column='Q225', blank=True, null=True)  # Field name made lowercase.
    q226 = models.TextField(db_column='Q226', blank=True, null=True)  # Field name made lowercase.
    q227 = models.TextField(db_column='Q227', blank=True, null=True)  # Field name made lowercase.
    q228 = models.TextField(db_column='Q228', blank=True, null=True)  # Field name made lowercase.
    q229 = models.TextField(db_column='Q229', blank=True, null=True)  # Field name made lowercase.
    q230 = models.TextField(db_column='Q230', blank=True, null=True)  # Field name made lowercase.
    q231 = models.TextField(db_column='Q231', blank=True, null=True)  # Field name made lowercase.
    q232 = models.TextField(db_column='Q232', blank=True, null=True)  # Field name made lowercase.
    q233 = models.TextField(db_column='Q233', blank=True, null=True)  # Field name made lowercase.
    q234 = models.TextField(db_column='Q234', blank=True, null=True)  # Field name made lowercase.
    q234a = models.TextField(db_column='Q234A', blank=True, null=True)  # Field name made lowercase.
    q235 = models.TextField(db_column='Q235', blank=True, null=True)  # Field name made lowercase.
    q236 = models.TextField(db_column='Q236', blank=True, null=True)  # Field name made lowercase.
    q237 = models.TextField(db_column='Q237', blank=True, null=True)  # Field name made lowercase.
    q238 = models.TextField(db_column='Q238', blank=True, null=True)  # Field name made lowercase.
    q239 = models.TextField(db_column='Q239', blank=True, null=True)  # Field name made lowercase.
    q240 = models.TextField(db_column='Q240', blank=True, null=True)  # Field name made lowercase.
    q241 = models.TextField(db_column='Q241', blank=True, null=True)  # Field name made lowercase.
    q242 = models.TextField(db_column='Q242', blank=True, null=True)  # Field name made lowercase.
    q243 = models.TextField(db_column='Q243', blank=True, null=True)  # Field name made lowercase.
    q244 = models.TextField(db_column='Q244', blank=True, null=True)  # Field name made lowercase.
    q245 = models.TextField(db_column='Q245', blank=True, null=True)  # Field name made lowercase.
    q246 = models.TextField(db_column='Q246', blank=True, null=True)  # Field name made lowercase.
    q247 = models.TextField(db_column='Q247', blank=True, null=True)  # Field name made lowercase.
    q248 = models.TextField(db_column='Q248', blank=True, null=True)  # Field name made lowercase.
    q249 = models.TextField(db_column='Q249', blank=True, null=True)  # Field name made lowercase.
    q250 = models.TextField(db_column='Q250', blank=True, null=True)  # Field name made lowercase.
    q251 = models.TextField(db_column='Q251', blank=True, null=True)  # Field name made lowercase.
    q252 = models.TextField(db_column='Q252', blank=True, null=True)  # Field name made lowercase.
    q253 = models.TextField(db_column='Q253', blank=True, null=True)  # Field name made lowercase.
    q254 = models.TextField(db_column='Q254', blank=True, null=True)  # Field name made lowercase.
    q255 = models.TextField(db_column='Q255', blank=True, null=True)  # Field name made lowercase.
    q256 = models.TextField(db_column='Q256', blank=True, null=True)  # Field name made lowercase.
    q257 = models.TextField(db_column='Q257', blank=True, null=True)  # Field name made lowercase.
    q258 = models.TextField(db_column='Q258', blank=True, null=True)  # Field name made lowercase.
    q259 = models.TextField(db_column='Q259', blank=True, null=True)  # Field name made lowercase.
    q260 = models.TextField(db_column='Q260', blank=True, null=True)  # Field name made lowercase.
    q261 = models.TextField(db_column='Q261', blank=True, null=True)  # Field name made lowercase.
    q262 = models.TextField(db_column='Q262', blank=True, null=True)  # Field name made lowercase.
    x003r2 = models.TextField(db_column='X003R2', blank=True, null=True)  # Field name made lowercase.
    x003r = models.TextField(blank=True, null=True)
    q263 = models.TextField(db_column='Q263', blank=True, null=True)  # Field name made lowercase.
    q264 = models.TextField(db_column='Q264', blank=True, null=True)  # Field name made lowercase.
    q265 = models.TextField(db_column='Q265', blank=True, null=True)  # Field name made lowercase.
    q266 = models.TextField(db_column='Q266', blank=True, null=True)  # Field name made lowercase.
    q267 = models.TextField(db_column='Q267', blank=True, null=True)  # Field name made lowercase.
    q268 = models.TextField(db_column='Q268', blank=True, null=True)  # Field name made lowercase.
    q269 = models.TextField(db_column='Q269', blank=True, null=True)  # Field name made lowercase.
    q270 = models.TextField(db_column='Q270', blank=True, null=True)  # Field name made lowercase.
    q271 = models.TextField(db_column='Q271', blank=True, null=True)  # Field name made lowercase.
    q272 = models.TextField(db_column='Q272', blank=True, null=True)  # Field name made lowercase.
    q273 = models.TextField(db_column='Q273', blank=True, null=True)  # Field name made lowercase.
    q274 = models.TextField(db_column='Q274', blank=True, null=True)  # Field name made lowercase.
    q275 = models.TextField(db_column='Q275', blank=True, null=True)  # Field name made lowercase.
    q275a = models.TextField(db_column='Q275A', blank=True, null=True)  # Field name made lowercase.
    q275r = models.TextField(db_column='Q275R', blank=True, null=True)  # Field name made lowercase.
    q276 = models.TextField(db_column='Q276', blank=True, null=True)  # Field name made lowercase.
    q276a = models.TextField(db_column='Q276A', blank=True, null=True)  # Field name made lowercase.
    q276r = models.TextField(db_column='Q276R', blank=True, null=True)  # Field name made lowercase.
    q277 = models.TextField(db_column='Q277', blank=True, null=True)  # Field name made lowercase.
    q277a = models.TextField(db_column='Q277A', blank=True, null=True)  # Field name made lowercase.
    q277r = models.TextField(db_column='Q277R', blank=True, null=True)  # Field name made lowercase.
    q278 = models.TextField(db_column='Q278', blank=True, null=True)  # Field name made lowercase.
    q278a = models.TextField(db_column='Q278A', blank=True, null=True)  # Field name made lowercase.
    q278r = models.TextField(db_column='Q278R', blank=True, null=True)  # Field name made lowercase.
    q279 = models.TextField(db_column='Q279', blank=True, null=True)  # Field name made lowercase.
    q280 = models.TextField(db_column='Q280', blank=True, null=True)  # Field name made lowercase.
    q281 = models.TextField(db_column='Q281', blank=True, null=True)  # Field name made lowercase.
    q282 = models.TextField(db_column='Q282', blank=True, null=True)  # Field name made lowercase.
    q283 = models.TextField(db_column='Q283', blank=True, null=True)  # Field name made lowercase.
    q284 = models.TextField(db_column='Q284', blank=True, null=True)  # Field name made lowercase.
    q285 = models.TextField(db_column='Q285', blank=True, null=True)  # Field name made lowercase.
    q286 = models.TextField(db_column='Q286', blank=True, null=True)  # Field name made lowercase.
    q287 = models.TextField(db_column='Q287', blank=True, null=True)  # Field name made lowercase.
    q288 = models.TextField(db_column='Q288', blank=True, null=True)  # Field name made lowercase.
    q288r = models.TextField(db_column='Q288R', blank=True, null=True)  # Field name made lowercase.
    q289 = models.TextField(db_column='Q289', blank=True, null=True)  # Field name made lowercase.
    q289cs9 = models.TextField(db_column='Q289CS9', blank=True, null=True)  # Field name made lowercase.
    q290 = models.TextField(db_column='Q290', blank=True, null=True)  # Field name made lowercase.
    y001 = models.TextField(db_column='Y001', blank=True, null=True)  # Field name made lowercase.
    y002 = models.TextField(db_column='Y002', blank=True, null=True)  # Field name made lowercase.
    y003 = models.TextField(db_column='Y003', blank=True, null=True)  # Field name made lowercase.
    sacsecval = models.TextField(db_column='SACSECVAL', blank=True, null=True)  # Field name made lowercase.
    resemaval = models.TextField(db_column='RESEMAVAL', blank=True, null=True)  # Field name made lowercase.
    i_authority = models.TextField(db_column='I_AUTHORITY', blank=True, null=True)  # Field name made lowercase.
    i_nationalism = models.TextField(db_column='I_NATIONALISM', blank=True, null=True)  # Field name made lowercase.
    i_devout = models.TextField(db_column='I_DEVOUT', blank=True, null=True)  # Field name made lowercase.
    defiance = models.TextField(db_column='DEFIANCE', blank=True, null=True)  # Field name made lowercase.
    i_religimp = models.TextField(db_column='I_RELIGIMP', blank=True, null=True)  # Field name made lowercase.
    i_religbel = models.TextField(db_column='I_RELIGBEL', blank=True, null=True)  # Field name made lowercase.
    i_religprac = models.TextField(db_column='I_RELIGPRAC', blank=True, null=True)  # Field name made lowercase.
    disbelief = models.TextField(db_column='DISBELIEF', blank=True, null=True)  # Field name made lowercase.
    i_norm1 = models.TextField(db_column='I_NORM1', blank=True, null=True)  # Field name made lowercase.
    i_norm2 = models.TextField(db_column='I_NORM2', blank=True, null=True)  # Field name made lowercase.
    i_norm3 = models.TextField(db_column='I_NORM3', blank=True, null=True)  # Field name made lowercase.
    relativism = models.TextField(db_column='RELATIVISM', blank=True, null=True)  # Field name made lowercase.
    i_trustarmy = models.TextField(db_column='I_TRUSTARMY', blank=True, null=True)  # Field name made lowercase.
    i_trustpolice = models.TextField(db_column='I_TRUSTPOLICE', blank=True, null=True)  # Field name made lowercase.
    i_trustcourts = models.TextField(db_column='I_TRUSTCOURTS', blank=True, null=True)  # Field name made lowercase.
    scepticism = models.TextField(db_column='SCEPTICISM', blank=True, null=True)  # Field name made lowercase.
    i_indep = models.TextField(db_column='I_INDEP', blank=True, null=True)  # Field name made lowercase.
    i_imagin = models.TextField(db_column='I_IMAGIN', blank=True, null=True)  # Field name made lowercase.
    i_nonobed = models.TextField(db_column='I_NONOBED', blank=True, null=True)  # Field name made lowercase.
    autonomy = models.TextField(db_column='AUTONOMY', blank=True, null=True)  # Field name made lowercase.
    i_womjob = models.TextField(db_column='I_WOMJOB', blank=True, null=True)  # Field name made lowercase.
    i_wompol = models.TextField(db_column='I_WOMPOL', blank=True, null=True)  # Field name made lowercase.
    i_womedu = models.TextField(db_column='I_WOMEDU', blank=True, null=True)  # Field name made lowercase.
    equality = models.TextField(db_column='EQUALITY', blank=True, null=True)  # Field name made lowercase.
    i_homolib = models.TextField(db_column='I_HOMOLIB', blank=True, null=True)  # Field name made lowercase.
    i_abortlib = models.TextField(db_column='I_ABORTLIB', blank=True, null=True)  # Field name made lowercase.
    i_divorlib = models.TextField(db_column='I_DIVORLIB', blank=True, null=True)  # Field name made lowercase.
    choice = models.TextField(db_column='CHOICE', blank=True, null=True)  # Field name made lowercase.
    i_voice1 = models.TextField(db_column='I_VOICE1', blank=True, null=True)  # Field name made lowercase.
    i_voice2 = models.TextField(db_column='I_VOICE2', blank=True, null=True)  # Field name made lowercase.
    i_voi2_00 = models.TextField(db_column='I_VOI2_00', blank=True, null=True)  # Field name made lowercase.
    voice = models.TextField(db_column='VOICE', blank=True, null=True)  # Field name made lowercase.
    secvalwgt = models.TextField(db_column='SECVALWGT', blank=True, null=True)  # Field name made lowercase.
    resemavalwgt = models.TextField(db_column='RESEMAVALWGT', blank=True, null=True)  # Field name made lowercase.
    fhregion = models.TextField(blank=True, null=True)
    polregfh = models.TextField(blank=True, null=True)
    freestfh = models.TextField(blank=True, null=True)
    prfhrat = models.TextField(blank=True, null=True)
    prfhscore = models.TextField(blank=True, null=True)
    clfhrat = models.TextField(blank=True, null=True)
    clfhscore = models.TextField(blank=True, null=True)
    democ = models.TextField(blank=True, null=True)
    autoc = models.TextField(blank=True, null=True)
    polity = models.TextField(blank=True, null=True)
    durable = models.TextField(blank=True, null=True)
    regtype = models.TextField(blank=True, null=True)
    ruleoflaw = models.TextField(blank=True, null=True)
    corrupttransp = models.TextField(blank=True, null=True)
    electintegr = models.TextField(blank=True, null=True)
    btiregion = models.TextField(blank=True, null=True)
    btistatus = models.TextField(blank=True, null=True)
    btidemstatus = models.TextField(blank=True, null=True)
    btistate = models.TextField(blank=True, null=True)
    btipolpart = models.TextField(blank=True, null=True)
    btiruleoflaw = models.TextField(blank=True, null=True)
    btistability = models.TextField(blank=True, null=True)
    btiintegration = models.TextField(blank=True, null=True)
    btimarket = models.TextField(blank=True, null=True)
    btigovindex = models.TextField(blank=True, null=True)
    btigoveperform = models.TextField(blank=True, null=True)
    btiregime = models.TextField(blank=True, null=True)
    regionwb = models.TextField(db_column='regionWB', blank=True, null=True)  # Field name made lowercase.
    incomewb = models.TextField(db_column='incomeWB', blank=True, null=True)  # Field name made lowercase.
    landwb = models.TextField(db_column='landWB', blank=True, null=True)  # Field name made lowercase.
    gdppercap1 = models.TextField(db_column='GDPpercap1', blank=True, null=True)  # Field name made lowercase.
    gdppercap2 = models.TextField(db_column='GDPpercap2', blank=True, null=True)  # Field name made lowercase.
    giniwb = models.TextField(db_column='giniWB', blank=True, null=True)  # Field name made lowercase.
    incrichest10p = models.TextField(blank=True, null=True)
    popwb1990 = models.TextField(db_column='popWB1990', blank=True, null=True)  # Field name made lowercase.
    popwb2000 = models.TextField(db_column='popWB2000', blank=True, null=True)  # Field name made lowercase.
    popwb2019 = models.TextField(db_column='popWB2019', blank=True, null=True)  # Field name made lowercase.
    lifeexpect = models.TextField(blank=True, null=True)
    popgrowth = models.TextField(blank=True, null=True)
    urbanpop = models.TextField(blank=True, null=True)
    laborforce = models.TextField(blank=True, null=True)
    deathrate = models.TextField(blank=True, null=True)
    unemployfem = models.TextField(blank=True, null=True)
    unemploymale = models.TextField(blank=True, null=True)
    unemploytotal = models.TextField(blank=True, null=True)
    accessclfuel = models.TextField(blank=True, null=True)
    accesselectr = models.TextField(blank=True, null=True)
    renewelectr = models.TextField(blank=True, null=True)
    co2emis = models.TextField(blank=True, null=True)
    co2percap = models.TextField(blank=True, null=True)
    easeofbusiness = models.TextField(blank=True, null=True)
    militaryexp = models.TextField(blank=True, null=True)
    trade = models.TextField(db_column='Trade', blank=True, null=True)  # Field name made lowercase.
    healthexp = models.TextField(blank=True, null=True)
    educationexp = models.TextField(blank=True, null=True)
    medageun = models.TextField(blank=True, null=True)
    meanschooling = models.TextField(blank=True, null=True)
    educationhdi = models.TextField(db_column='educationHDI', blank=True, null=True)  # Field name made lowercase.
    compulseduc = models.TextField(blank=True, null=True)
    gii = models.TextField(db_column='GII', blank=True, null=True)  # Field name made lowercase.
    dgi = models.TextField(db_column='DGI', blank=True, null=True)  # Field name made lowercase.
    womenparl = models.TextField(blank=True, null=True)
    hdi = models.TextField(blank=True, null=True)
    incomeindexhdi = models.TextField(db_column='incomeindexHDI', blank=True, null=True)  # Field name made lowercase.
    humanineqiality = models.TextField(blank=True, null=True)
    lifeexpecthdi = models.TextField(db_column='lifeexpectHDI', blank=True, null=True)  # Field name made lowercase.
    homiciderate = models.TextField(blank=True, null=True)
    refugeesorigin = models.TextField(db_column='Refugeesorigin', blank=True, null=True)  # Field name made lowercase.
    internetusers = models.TextField(blank=True, null=True)
    mobphone = models.TextField(blank=True, null=True)
    migrationrate = models.TextField(blank=True, null=True)
    schoolgpi = models.TextField(blank=True, null=True)
    femchoutsch = models.TextField(blank=True, null=True)
    choutsch = models.TextField(blank=True, null=True)
    v2x_polyarchy = models.TextField(blank=True, null=True)
    v2x_libdem = models.TextField(blank=True, null=True)
    v2x_partipdem = models.TextField(blank=True, null=True)
    v2x_delibdem = models.TextField(blank=True, null=True)
    v2x_egaldem = models.TextField(blank=True, null=True)
    v2x_freexp_altinf = models.TextField(blank=True, null=True)
    v2x_frassoc_thick = models.TextField(blank=True, null=True)
    v2xel_frefair = models.TextField(blank=True, null=True)
    v2xcl_rol = models.TextField(blank=True, null=True)
    v2x_cspart = models.TextField(blank=True, null=True)
    v2xeg_eqdr = models.TextField(blank=True, null=True)
    v2excrptps = models.TextField(blank=True, null=True)
    v2exthftps = models.TextField(blank=True, null=True)
    v2juaccnt = models.TextField(blank=True, null=True)
    v2cltrnslw = models.TextField(blank=True, null=True)
    v2clacjust = models.TextField(blank=True, null=True)
    v2clsocgrp = models.TextField(blank=True, null=True)
    v2clacfree = models.TextField(blank=True, null=True)
    v2clrelig = models.TextField(blank=True, null=True)
    v2csrlgrep = models.TextField(blank=True, null=True)
    v2mecenefm = models.TextField(blank=True, null=True)
    v2mecenefi = models.TextField(blank=True, null=True)
    v2mebias = models.TextField(blank=True, null=True)
    v2pepwrses = models.TextField(blank=True, null=True)
    v2pepwrgen = models.TextField(blank=True, null=True)
    v2peedueq = models.TextField(blank=True, null=True)
    v2pehealth = models.TextField(blank=True, null=True)
    v2peapsecon = models.TextField(blank=True, null=True)
    v2peasjsoecon = models.TextField(blank=True, null=True)
    v2clgencl = models.TextField(blank=True, null=True)
    v2peasjgen = models.TextField(blank=True, null=True)
    v2peasbgen = models.TextField(blank=True, null=True)
    v2cafres = models.TextField(blank=True, null=True)
    v2cafexch = models.TextField(blank=True, null=True)
    v2x_corr = models.TextField(blank=True, null=True)
    v2x_gender = models.TextField(blank=True, null=True)
    v2x_gencl = models.TextField(blank=True, null=True)
    v2x_genpp = models.TextField(blank=True, null=True)
    v2x_rule = models.TextField(blank=True, null=True)
    v2xcl_acjst = models.TextField(blank=True, null=True)
    id_gps = models.TextField(db_column='ID_GPS', blank=True, null=True)  # Field name made lowercase.
    id_partyfacts = models.TextField(db_column='ID_PartyFacts', blank=True, null=True)  # Field name made lowercase.
    partyname = models.TextField(db_column='Partyname', blank=True, null=True)  # Field name made lowercase.
    partyabb = models.TextField(db_column='Partyabb', blank=True, null=True)  # Field name made lowercase.
    cparty = models.TextField(db_column='CPARTY', blank=True, null=True)  # Field name made lowercase.
    cpartyabb = models.TextField(db_column='CPARTYABB', blank=True, null=True)  # Field name made lowercase.
    type_values = models.TextField(db_column='Type_Values', blank=True, null=True)  # Field name made lowercase.
    type_populism = models.TextField(db_column='Type_Populism', blank=True, null=True)  # Field name made lowercase.
    type_populist_values = models.TextField(db_column='Type_Populist_Values', blank=True, null=True)  # Field name made lowercase.
    type_partysize_vote = models.TextField(db_column='Type_Partysize_vote', blank=True, null=True)  # Field name made lowercase.
    type_partysize_seat = models.TextField(db_column='Type_Partysize_seat', blank=True, null=True)  # Field name made lowercase.
    gps_v4_scale = models.TextField(db_column='GPS_V4_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v6_scale = models.TextField(db_column='GPS_V6_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v8_scale = models.TextField(db_column='GPS_V8_Scale', blank=True, null=True)  # Field name made lowercase.
    gps_v9 = models.TextField(db_column='GPS_V9', blank=True, null=True)  # Field name made lowercase.
    gps_v10 = models.TextField(db_column='GPS_V10', blank=True, null=True)  # Field name made lowercase.
    gps_v11 = models.TextField(db_column='GPS_V11', blank=True, null=True)  # Field name made lowercase.
    gps_v12 = models.TextField(db_column='GPS_V12', blank=True, null=True)  # Field name made lowercase.
    gps_v13 = models.TextField(db_column='GPS_V13', blank=True, null=True)  # Field name made lowercase.
    gps_v14 = models.TextField(db_column='GPS_V14', blank=True, null=True)  # Field name made lowercase.
    gps_v15 = models.TextField(db_column='GPS_V15', blank=True, null=True)  # Field name made lowercase.
    gps_v16 = models.TextField(db_column='GPS_V16', blank=True, null=True)  # Field name made lowercase.
    gps_v17 = models.TextField(db_column='GPS_V17', blank=True, null=True)  # Field name made lowercase.
    wvs_lr_partyvoter = models.TextField(db_column='WVS_LR_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_libcon_partyvoter = models.TextField(db_column='WVS_LibCon_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_polmistrust_partyvoter = models.TextField(db_column='WVS_Polmistrust_PartyVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_lr_medianvoter = models.TextField(db_column='WVS_LR_MedianVoter', blank=True, null=True)  # Field name made lowercase.
    wvs_libcon_medianvoter = models.TextField(db_column='WVS_LibCon_MedianVoter', blank=True, null=True)  # Field name made lowercase.
    v2psbars = models.TextField(blank=True, null=True)
    v2psorgs = models.TextField(blank=True, null=True)
    v2psprbrch = models.TextField(blank=True, null=True)
    v2psprlnks = models.TextField(blank=True, null=True)
    v2psplats = models.TextField(blank=True, null=True)
    v2xnp_client = models.TextField(blank=True, null=True)
    v2xps_party = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_large'


class WorldFertility(models.Model):
    country = models.CharField(max_length=-1, blank=True, null=True)
    fertility = models.FloatField(blank=True, null=True)
    iso_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_fertility'


class WorldGdpPerCap(models.Model):
    country = models.CharField(max_length=-1, blank=True, null=True)
    gdp_per_cap = models.FloatField(blank=True, null=True)
    iso_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_gdp_per_cap'
