class ComponentAddition:

    def __init__(self):
        self.arr = {"name": "sample-name", "type": "sample-type", "flavor": "sample-flavor", "description": "sample"}

    @staticmethod
    def comp_add():
        print("Enter the Name of Component to be added")
        comp_name = input()
        print("Enter the Type of Components")
        comp_type = input()
        print("Enter the Flavor of the component")
        comp_flavor = input()
        print("Enter a Description for the Component")
        comp_desc = input()

        # Adding those new components in the shape of array:
        data = {"name": comp_name, "type": comp_type, "flavor": comp_flavor, "description": comp_desc}
        return data
