import random



print("""
A Lv. 100 Raichu (Electric, Sp. Atk: 306) attacks a Lv. 100 Lugia (Physic/Flying, Sp. Def: 447) with Static Ability, a Electric-type move
with a Power of  and gains a same-type attack bonus.. It hits the target normally but deals a not very effective damage. The
weather on the field is normal. Given the following conditions, determine how much damage Raichu attack will deal.
""")

print ("""
Pokemon Name : Raichu   Level : 100
Type: Electric
Sp. Attack : 306
Power : Static Ability 

VS:


Pokemon name: Lugia   Level : 100
Type : Physic/Flying
Sp. Defense : 447""")

#modifier
target = 1
weather =1
badge = 1
crit = random.randint(1,2)
randomm = round(random.uniform(0.85 , 1.00),2)
stab = 1
type = round(random.uniform(0.25 , 0.50),2)
opt = random.randint(0,1)
if opt ==0:
    burn=0.5
elif opt ==1:
    burn=1
other = 1

modifier = target * weather * badge * crit * randomm * stab * type * burn * other
damage =round(((((((2*100)/5)+2)*306)*(306/447))/50)+2)*modifier
fdamage= damage * modifier

print(f"""
MODIFIERS:

target :    {target}
weather :   {weather}
badge :     {badge}
crit :      {crit}
random :    {randomm}
stab :      {stab}
type :      {type}
burn :      {burn}
other :     {other}

total damage :      {damage}
total modifier :    {modifier}
Your final damage:  {round((fdamage),2)} """)