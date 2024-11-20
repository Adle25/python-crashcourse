def build_profile(first, last, **user_info ):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

adilet = build_profile('Adilet', 'Askar', education='Master degree', city='Almaty', job='Software developer')
print(adilet)