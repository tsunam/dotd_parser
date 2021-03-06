def load_proc_to_names():
    enchantments_translation = {}
    generals_translation = {}
    mounts_translation = {}
    equipment_translation = {}
    troops_translation = {}
    legions_translation = {}
    engineering_translation = {}

    enchantment_dawn_list =  db().select(db.dawn_enchantments.name, db.dawn_enchantments.proc_name, db.dawn_enchantments.equipType)
    gen_dawn_list = db().select(db.dawn_generals.name, db.dawn_generals.proc_name, db.dawn_generals.equipType)
    mount_dawn_list = db().select(db.dawn_mounts.name, db.dawn_mounts.proc_name, db.dawn_mounts.equipType)
    equip_dawn_list = db().select(db.dawn_equipment.name, db.dawn_equipment.proc_name, db.dawn_equipment.equipType)
    troop_dawn_list = db().select(db.dawn_troops.name, db.dawn_troops.proc_name, db.dawn_troops.equipType)
    legion_dawn_list = db().select(db.dawn_legions.name, db.dawn_legions.proc_name, db.dawn_legions.equipType)

    enchantment_suns_list =  db().select(db.suns_enchantments.name, db.suns_enchantments.proc_name, db.suns_enchantments.equipType)
    gen_suns_list = db().select(db.suns_generals.name, db.suns_generals.proc_name, db.suns_generals.equipType)
    mount_suns_list = db().select(db.suns_mounts.name, db.suns_mounts.proc_name, db.suns_mounts.equipType)
    equip_suns_list = db().select(db.suns_equipment.name, db.suns_equipment.proc_name, db.suns_equipment.equipType)
    troop_suns_list = db().select(db.suns_troops.name, db.suns_troops.proc_name, db.suns_troops.equipType)
    legion_suns_list = db().select(db.suns_legions.name, db.suns_legions.proc_name, db.suns_legions.equipType)
    engineering_suns_list = db().select(db.suns_engineering.name, db.suns_engineering.proc_name, db.suns_engineering.equipType)

    for row in gen_dawn_list:
        if len(row.proc_name):
            generals_translation[row.proc_name] = [row.name,row.equipType]

    for row in gen_suns_list:
        if len(row.proc_name):
            generals_translation[row.proc_name] = [row.name,row.equipType]

    for row in mount_dawn_list:
        if len(row.proc_name):
            mounts_translation[row.proc_name] = [row.name,row.equipType]

    for row in mount_suns_list:
        if len(row.proc_name):
            mounts_translation[row.proc_name] = [row.name,row.equipType]

    for row in equip_dawn_list:
        if len(row.proc_name):
            equipment_translation[row.proc_name] = [row.name,row.equipType]

    for row in equip_suns_list:
        if len(row.proc_name):
            equipment_translation[row.proc_name] = [row.name,row.equipType]

    for row in troop_dawn_list:
        if len(row.proc_name):
            troops_translation[row.proc_name] = [row.name,row.equipType] 

    for row in troop_suns_list:
        if len(row.proc_name):
            troops_translation[row.proc_name] = [row.name,row.equipType]

    for row in legion_dawn_list:
        if len(row.proc_name):
            legions_translation[row.proc_name] = [row.name,row.equipType]

    for row in legion_suns_list:
        if len(row.proc_name):
            legions_translation[row.proc_name] = [row.name,row.equipType]

    for row in engineering_suns_list:
        if len(row.proc_name):
            engineering_translation[row.proc_name] = [row.name,row.equipType]

    for row in enchantment_dawn_list:
        if len(row.proc_name):
            enchantments_translation[row.proc_name] = [row.name,row.equipType]

    for row in enchantment_suns_list:
        if len(row.proc_name):
            enchantments_translation[row.proc_name] = [row.name,row.equipType]

    return [generals_translation, mounts_translation,
            equipment_translation, troops_translation,
            legions_translation, engineering_translation,
	    enchantments_translation]
