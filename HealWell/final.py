from Available_Services.admin import setup_services
from patient_details.patient import get_patient
from Display_services.services import display_services, select_services
from Cost_Of_Services.services_cost import get_selected
from Total_Cost.cost import subtotal
from Discounts.discount import discount
from Apply_GST.gst import gst
from Display_Invoice.Invoice import invoice

def main():
    try:
        services, costs = setup_services()
        patient = get_patient()
        display_services(services)
        indexes = select_services()
        sel_s, sel_c = get_selected(services, costs, indexes)
        sub = subtotal(sel_c)
        after_disc, disc = discount(sub, patient[1])
        g, total = gst(after_disc)
        invoice(patient, sel_s, sel_c, sub, disc, g, total)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
