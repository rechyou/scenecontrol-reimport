
def enable_effect_array(defines, properties):
    enableEffect = []
    for v in defines:
        if properties.pop(0):
            enableEffect.append(f"'{v}'")
    return '{' + ','.join(enableEffect) + '}'
