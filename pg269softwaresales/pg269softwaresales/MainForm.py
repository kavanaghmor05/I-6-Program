import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(19, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(272, 107)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Quantity Sold"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(260, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Package A:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(260, 29)
		self._label2.TabIndex = 1
		self._label2.Text = "Package B:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 74)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(260, 29)
		self._label3.TabIndex = 2
		self._label3.Text = "Package C:"
		self._label3.Click += self.Label3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(125, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(141, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(125, 48)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(141, 20)
		self._textBox2.TabIndex = 3
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(125, 77)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(141, 20)
		self._textBox3.TabIndex = 4
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Location = System.Drawing.Point(19, 136)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(272, 91)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Price Total"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label4.Location = System.Drawing.Point(6, 16)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(260, 17)
		self._label4.TabIndex = 0
		self._label4.Text = "Package A:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Location = System.Drawing.Point(6, 33)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(260, 17)
		self._label5.TabIndex = 1
		self._label5.Text = "Package B:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label6.Location = System.Drawing.Point(6, 50)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(260, 17)
		self._label6.TabIndex = 2
		self._label6.Text = "Package C:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label7.Location = System.Drawing.Point(6, 67)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(260, 17)
		self._label7.TabIndex = 3
		self._label7.Text = "Grand Total:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(300, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 31)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(297, 196)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 31)
		self._button2.TabIndex = 3
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(300, 100)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 31)
		self._button3.TabIndex = 4
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(413, 235)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg269softwaresales"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		A = self._textBox1.Text
		B = self._textBox2.Text
		C = self._textBox3.Text
		AP = 99
		BP = 199
		CP = 299
		ATP = A * AP
		BTP = B * BP
		CTP = C * CP
		if A in range (1, 11):
			self._label4.Text = "Package A: " + str(ATP)
		elif A in range (11, 20):
			ADis = ATP * 0.2
			DATP = ATP - ADis
			self.label4.Text = "Package A: " + str(DATP)
		elif A in range (20, 48):
			ADis = ATP * 

	def Button3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()