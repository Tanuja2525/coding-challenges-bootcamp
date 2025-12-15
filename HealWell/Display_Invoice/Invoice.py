def invoice(patient, services, costs, sub, disc, gst, total):
    name, age, gender, contact = patient

    print("\nHealWell Care Hospital")
    print("Patient Invoice")
    print("-" * 40)

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Contact: {contact}")

    print("\nServices Availed:")
    for i, (s, c) in enumerate(zip(services, costs), 1):
        print(f"{i}. {s}: ₹{c}")

    print(f"\nSubtotal: ₹{sub}")
    print(f"Discount: ₹{disc}")
    print(f"GST (18%): ₹{gst}")
    print(f"Grand Total: ₹{total}")
