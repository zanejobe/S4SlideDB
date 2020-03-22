-- SHOW DATABASES

CREATE DATABASE s4slide; 

USE s4slide;

/**********************************************************************
 * SUMMARY_INFO_ID
 * 
 * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
 *      - Parent ID
 *      - Object Type 
 **********************************************************************/
CREATE TABLE summary_info_id (
    id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    pid INT,
    name VARCHAR(50),
    aliases VARCHAR(50), 
    frontal_confinement BIT(1),
    object_type BIT(1),
    ss_depth_m FLOAT,
    ss_time_twtt FLOAT,
    ss_depth_notes LONGTEXT
);

/**********************************************************************
 * LANDSLIDE MORPHOMETRICS
 *
 * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
 *      - Scarp Surf Nat 
 *          - What kind of data type is this? String?
 *          - If it is a string, how long should the string be
 **********************************************************************/
CREATE TABLE landslide_morphometrics (
    id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    landslide_id INT UNSIGNED NOT NULL REFERENCES summary_info_id(id),
    latitude FLOAT,
    longitude FLOAT,
    w_depth_min FLOAT,
    w_depth_max FLOAT, 
    w_depth_notes LONGTEXT,
    lt FLOAT,
    ld FLOAT, 
    le FLOAT, 
    l_notes LONGTEXT,
    ls FLOAT,
    hs FLOAT,
    he FLOAT,
    ws FLOAT,
    scarp_surf_nat VARCHAR(50),
    scarp_notes LONGTEXT,
    wd FLOAT,
    td_max_m FLOAT,
    td_max_twtt FLOAT,
    tu_max_m FLOAT,
    tu_max_twtt FLOAT,
    t_notes LONGTEXT,
    dep_notes LONGTEXT,
    ht FLOAT, 
    s FLOAT, 
    s_notes LONGTEXT,
    ss FLOAT,
    ss_notes LONGTEXT,
    st FLOAT, 
    st_notes LONGTEXT
);

/**********************************************************************
 * LANDSLIDE METRICS
 *
 * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
 *      - Age error
 **********************************************************************/
CREATE TABLE landslide_metrics (
    id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    landslide_id INT UNSIGNED NOT NULL REFERENCES summary_info_id(id),
    attachment BIT(1),
    surf_basal VARCHAR(50),
    surf_upper VARCHAR(50),
    a FLOAT,
    a_notes LONGTEXT,
    v FLOAT,
    v_notes LONGTEXT, 
    age INT,
    age_error BIT(1),
    age_notes LONGTEXT,
    features LONGTEXT
);

/**********************************************************************
 * META TABLE
 *
 * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
 *      - Data Sources (strictly a link?)
 *      - Data Repo (strictly a link?)
 *      - Pub (strictly a link?)
 *      - Data resolution horizontal 
 *          - (is this an int or float, what are the units)
 *          - what are the units on this? pixel?
 *      - Data resolution vertical 
 *          - (is this an int or float, what are the units)
 *          - what are the units on this? pixel?
 **********************************************************************/
CREATE TABLE meta_table (
    id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    landslide_id INT UNSIGNED NOT NULL REFERENCES summary_info_id(id),
    data_type VARCHAR(50), 
    data_type_notes LONGTEXT,
    data_source VARCHAR(100),
    data_repo VARCHAR(100),
    pub VARCHAR(100),
    contact_name VARCHAR(50),
    contact_email VARCHAR(50), 
    db_contact_name VARCHAR(50),
    db_contact_email VARCHAR(50),
    db_notes LONGTEXT,
    data_res_h INT,
    data_res_v INT,
    notes LONGTEXT
);


