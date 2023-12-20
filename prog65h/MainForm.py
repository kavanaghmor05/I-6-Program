import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 156)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 44)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(122, 156)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 44)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(232, 156)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 44)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Cyan
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(156, 30)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Pounds:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Cyan
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(12, 39)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(156, 30)
		self._label2.TabIndex = 4
		self._label2.Text = "Enter Shillings:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cyan
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(12, 69)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(156, 30)
		self._label3.TabIndex = 5
		self._label3.Text = "Enter Pence:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Fuchsia
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 117)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(335, 27)
		self._label4.TabIndex = 6
		self._label4.Text = "Decimal Pounds:"
		self._label4.Click += self.Label4Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(174, 15)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(173, 20)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(174, 45)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(173, 20)
		self._textBox2.TabIndex = 8
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(174, 75)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(173, 20)
		self._textBox3.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(367, 209)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog65h"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label4.Text = "Decimal Pounds: "

	def Button1Click(self, sender, e):
		P = float(self._textBox1.Text)
		S = float(self._textBox2.Text)
		p = float(self._textBox3.Text)
		#240 pence to an old pound, 100 pence to a new pound
		S2 = S * 12
		P2 = P * 240
		AlmTot = P2 + S2 + p
		Total = AlmTot / 100
		self._label4.Text = "Decimal Pound: " + str(Total)