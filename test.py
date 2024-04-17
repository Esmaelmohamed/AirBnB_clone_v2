def do_create(self, arg):
    if arg:
        try:
            args = arg.split()
            class_name = args[0]

            if class_name in models.classes:
                template = models.classes[class_name]
                new_instance = template()

                # Iterate through the parameters
                for param in args[1:]:
                    key_value = param.split("=")
                    if len(key_value) != 2:
                        print("** Invalid parameter format: {} **".format(param))
                        continue

                    key = key_value[0]
                    value = key_value[1]

                    # Handle different value types according to the specified syntax
                    if value.startswith('"') and value.endswith('"'):
                        # String value
                        value = value[1:-1].replace('\\"', '"').replace('_', ' ')
                    elif '.' in value:
                        # Float value
                        try:
                            value = float(value)
                        except ValueError:
                            print("** Invalid float value for parameter {}: {} **".format(key, value))
                            continue
                    else:
                        # Integer value
                        try:
                            value = int(value)
                        except ValueError:
                            print("** Invalid integer value for parameter {}: {} **".format(key, value))
                            continue

                    # Set the attribute of the new instance
                    setattr(new_instance, key, value)

                new_instance.save()
                print(new_instance.id)
            else:
                print("** Class doesn't exist **")
        except Exception as e:
            print("** Error creating instance: {} **".format(e))
    else:
        print("** Class name missing **")
