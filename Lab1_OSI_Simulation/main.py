import sys
from layers.physical_layer import PhysicalLayer
from layers.datalink_layer import DataLinkLayer
from layers.network_layer import NetworkLayer
from layers.transport import TransportLayer
from layers.session import SessionLayer
from layers.presentation_layer import PresentationLayer
from layers.application import ApplicationLayer

def run_sender():
    """Simulates the sender (client) side."""
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    data_link = DataLinkLayer()
    phys = PhysicalLayer(role="client")

    # Start connection
    phys.start_connection()

    # Application Layer
    message = input("Enter your message: ")
    message = app.generate_request(message)
    print("[Application Layer]:", message)

    # Presentation Layer
    encrypted_message = pres.encrypt(message)
    print("[Presentation Layer]:", encrypted_message)

    # Session Layer
    sess.start_session()
    session_data = sess.encapsulate(encrypted_message)

    # Transport Layer
    segmented_data = trans.encapsulate(session_data)

    # Network Layer
    packet = net.encapsulate(segmented_data)

    # Data Link Layer
    framed_data = data_link.encapsulate(packet)

    # Physical Layer (send)
    phys.send_bits(framed_data)
    print("[Physical Layer]: Data sent.")

    # Close connection
    phys.close_connection()

def run_receiver():
    """Simulates the receiver (server) side."""
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    data_link = DataLinkLayer()
    phys = PhysicalLayer(role="server")

    # Start connection
    phys.start_connection()
    print("[Physical Layer]: Waiting for data...")

    # Receive Data
    received_data = phys.receive_bits()
    print("[Physical Layer]: Data received.")

    # Data Link Layer
    packet = data_link.decapsulate(received_data)

    # Network Layer
    segmented_data = net.decapsulate(packet)

    # Transport Layer
    session_data = trans.decapsulate(segmented_data)

    # Session Layer
    decrypted_session = sess.decapsulate(session_data)

    # Presentation Layer
    decrypted_message = pres.decrypt(decrypted_session)

    # Application Layer
    print("[Final Decoded Message]:", decrypted_message)

    # Close connection
    phys.close_connection()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [server|client]")
        sys.exit(1)

    role = sys.argv[1].lower()
    if role == "server":
        run_receiver()
    elif role == "client":
        run_sender()
    else:
        print("Invalid role! Use 'server' or 'client'.")
