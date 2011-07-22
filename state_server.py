import zmq
import struct

class StateMsg(object):
	Attenuation = 0

	def __init__(self, state_type):
		self.state_type = state_type

	def __str__(self):
		return struct.pack("B", self.struct)

class AtennuationMsg(StateMsg):
	Roll = 0
	Pitch = 1
	Yaw = 2
	X = 3
	Y = 4
	Z = 5

	def __init__(self, axis, value):
		StateMsg.__init__(self, StateMsg.Attenuation)
		self.axis = axis
		self.value = value

	def __str__(self):
		return StateMsg.__str__(self) + struct.pack("Bf", self.axis, self.value)

class StateServer(object):
	def __init__(self, zmq_context):
		self.context = zmq_context
		self.socket = self.context.socket(zmq.PUB)

	def bind(self, bind_address):
		self.socket.bind(bind_address)

if __name__ == "__main__":
	ss = StateServer(zmq.Context())
	ss.bind("tcp://127.0.0.1:5000")

