print("This is your Shipping Label:")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for value in kwargs.values():
    #     print(value)

    if "apt" in kwargs:
        print(kwargs.get("Street"), kwargs.get("apt"))
    elif "PO_BOX" in kwargs:
        print(kwargs.get("Street"))
        print(kwargs.get("PO_BOX"))
    else:
        print(kwargs.get("Street"))
    print(kwargs.get("Country"), kwargs.get("City"), kwargs.get("Pin_Code"))

shipping_label(
    "Ms.", "Prerna", "Singhal",
      Street = "Hadapsar",
      apt = "100",
      PO_BOX = "PO BOX 1001",
      Country = "India",
      City = "Pune",
      Pin_Code = "411056"
    )


