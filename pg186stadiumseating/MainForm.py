import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._TickSold = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._classC = System.Windows.Forms.Label()
		self._classB = System.Windows.Forms.Label()
		self._classA = System.Windows.Forms.Label()
		self._toterev = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._TickSold.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# TickSold
		# 
		self._TickSold.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._TickSold.Controls.Add(self._textBox3)
		self._TickSold.Controls.Add(self._textBox2)
		self._TickSold.Controls.Add(self._textBox1)
		self._TickSold.Controls.Add(self._label4)
		self._TickSold.Controls.Add(self._label3)
		self._TickSold.Controls.Add(self._label2)
		self._TickSold.Controls.Add(self._label1)
		self._TickSold.Location = System.Drawing.Point(12, 12)
		self._TickSold.Name = "TickSold"
		self._TickSold.Size = System.Drawing.Size(264, 160)
		self._TickSold.TabIndex = 0
		self._TickSold.TabStop = False
		self._TickSold.Text = "Tickets Sold"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(265, 52)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the amount of tickets sold per class seat"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 68)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Class A:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 91)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Class B:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(6, 114)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Class C:"
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._groupBox1.Controls.Add(self._classC)
		self._groupBox1.Controls.Add(self._classB)
		self._groupBox1.Controls.Add(self._classA)
		self._groupBox1.Controls.Add(self._toterev)
		self._groupBox1.Location = System.Drawing.Point(282, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(303, 160)
		self._groupBox1.TabIndex = 4
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Revenue Generated"
		# 
		# classC
		# 
		self._classC.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._classC.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._classC.Location = System.Drawing.Point(6, 114)
		self._classC.Name = "classC"
		self._classC.Size = System.Drawing.Size(243, 23)
		self._classC.TabIndex = 3
		self._classC.Text = "Class C:"
		# 
		# classB
		# 
		self._classB.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._classB.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._classB.Location = System.Drawing.Point(6, 91)
		self._classB.Name = "classB"
		self._classB.Size = System.Drawing.Size(243, 23)
		self._classB.TabIndex = 2
		self._classB.Text = "Class B:"
		# 
		# classA
		# 
		self._classA.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._classA.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._classA.Location = System.Drawing.Point(6, 68)
		self._classA.Name = "classA"
		self._classA.Size = System.Drawing.Size(243, 23)
		self._classA.TabIndex = 1
		self._classA.Text = "Class A:"
		# 
		# toterev
		# 
		self._toterev.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._toterev.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._toterev.Location = System.Drawing.Point(6, 16)
		self._toterev.Name = "toterev"
		self._toterev.Size = System.Drawing.Size(291, 27)
		self._toterev.TabIndex = 0
		self._toterev.Text = "Total Revenue:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 178)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 37)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(219, 178)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 37)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(467, 178)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(118, 37)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(112, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(146, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(112, 94)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(146, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(112, 117)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(146, 20)
		self._textBox3.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.White
		self.ClientSize = System.Drawing.Size(597, 228)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._TickSold)
		self.Name = "MainForm"
		self.Text = "pg186stadiumseating"
		self._TickSold.ResumeLayout(False)
		self._TickSold.PerformLayout()
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._textBox3.Clear()
		self._toterev.Text = "Total Revenue:"
		self._classA.Text = "Class A: "
		self._classB.Text = "Class B: "
		self._classC.Text = "Class C: "

	def Button1Click(self, sender, e):
		cA = 0.0
		cB = 0.0
		cC = 0.0
		Acost = 15
		Bcost = 12
		Ccost = 9
		cA = float(self._textBox1.Text)
		cB = float(self._textBox2.Text)
		cC = float(self._textBox3.Text)
		Arev = Acost * cA
		Brev = Bcost * cB
		Crev = Ccost * cC
		ToteRev = Arev + Brev + Crev
		self._toterev.Text = "Total Revenue: $" + str(ToteRev)
		self._classA.Text = "Class A: $" + str(Arev)
		self._classB.Text = "Class B: $" + str(Brev)
		self._classC.Text = "Class C: $" + str(Crev)
		