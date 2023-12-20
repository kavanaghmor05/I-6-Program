import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._ASal = System.Windows.Forms.Label()
		self._PayP = System.Windows.Forms.Label()
		self._SalPPay = System.Windows.Forms.Label()
		self._Calculate = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# ASal
		# 
		self._ASal.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._ASal.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._ASal.Location = System.Drawing.Point(12, 9)
		self._ASal.Name = "ASal"
		self._ASal.Size = System.Drawing.Size(145, 27)
		self._ASal.TabIndex = 0
		self._ASal.Text = "Anual Salary:"
		# 
		# PayP
		# 
		self._PayP.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._PayP.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._PayP.Location = System.Drawing.Point(12, 36)
		self._PayP.Name = "PayP"
		self._PayP.Size = System.Drawing.Size(229, 27)
		self._PayP.TabIndex = 1
		self._PayP.Text = "Pay Periods Per Year:"
		# 
		# SalPPay
		# 
		self._SalPPay.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._SalPPay.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._SalPPay.Location = System.Drawing.Point(12, 63)
		self._SalPPay.Name = "SalPPay"
		self._SalPPay.Size = System.Drawing.Size(405, 27)
		self._SalPPay.TabIndex = 2
		self._SalPPay.Text = "Salary Per Pay Period:"
		# 
		# Calculate
		# 
		self._Calculate.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Calculate.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Calculate.Location = System.Drawing.Point(140, 93)
		self._Calculate.Name = "Calculate"
		self._Calculate.Size = System.Drawing.Size(124, 33)
		self._Calculate.TabIndex = 3
		self._Calculate.Text = "Calculate"
		self._Calculate.UseVisualStyleBackColor = False
		self._Calculate.Click += self.CalculateClick
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(163, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(170, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(247, 39)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(170, 20)
		self._textBox2.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(425, 131)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._Calculate)
		self.Controls.Add(self._SalPPay)
		self.Controls.Add(self._PayP)
		self.Controls.Add(self._ASal)
		self.Name = "MainForm"
		self.Text = "pg153salarycalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def CalculateClick(self, sender, e):
		ASal = 0.0
		PayP = 0.0
		Sal = 0.0
		ASal = float(self._textBox1.Text)
		PayP = int(self._textBox2.Text)
		Sal = ASal/PayP
		self._SalPPay.Text = "Salary Per Pay Period: " + str(round(Sal,2))