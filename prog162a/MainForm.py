import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(173, 25)
		self._label1.TabIndex = 1
		self._label1.Text = "Number:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(95, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(225, 20)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 50)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(308, 28)
		self._label2.TabIndex = 3
		self._label2.Text = "Factorial of ..."
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 81)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 39)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(114, 81)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 39)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlText
		self._button3.Location = System.Drawing.Point(220, 81)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 39)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self.ClientSize = System.Drawing.Size(332, 135)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label2.Text = "Factorial: "

	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		if num < 0:
			self._label2.Text = "Factorial does not exist for negative number"
		elif num == 0:
			self._label2.Text = "Factorial of 0 is 1"
		else:
			factorial(n)
			factorial = 1
			for i in range(n):
				factorial*=i+1
			return factorial
			self._label2.Text = "Factorial of " + str(num) + " is " + str(factorial)
			
			