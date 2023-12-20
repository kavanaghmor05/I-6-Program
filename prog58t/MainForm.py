import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(168, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(118, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(168, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 25)
		self._label1.TabIndex = 2
		self._label1.Text = "Price:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 34)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 26)
		self._label2.TabIndex = 3
		self._label2.Text = "Received:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 108)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(274, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Dollars:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 131)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(274, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Quaters:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 154)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(274, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Dimes:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 177)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(274, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "Nickels:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 200)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(274, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "Pennies:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(292, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 43)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(291, 97)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 43)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(291, 177)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 43)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(12, 75)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(274, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "Change:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(397, 232)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog58t"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Appliation.Exit()

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""

	def Button1Click(self, sender, e):
		P = float(self._textBox1.Text)
		R = float(self._textBox2.Text)
		Change = R - P
		self._label8.Text = "Change: " + str(Change)
		dollar = math. floor(Change)
		q = Change - dollar
		quart = q / 0.25
		quarter = math. floor(quart)
		d = q - (0.25 * quarter)
		di = d / 0.10
		dime = math. floor(di)
		n = d - (dime * 0.10)
		nick = n / 0.05
		nickel = math. floor (nick)
		p = n - (nickel * 0.05)
		pen = p / 0.01
		penny = math. floor(pen)
		self._label8.Text = str(Change)
		self._label3.Text = "Dollars: " + str(dollar)
		self._label4.Text = "Quarters: " + str(quarter)
		self._label5.Text = "Dimes: " + str(dime)
		self._label6.Text = "Nickels: " + str(nickel)
		self._label7.Text = "Pennies: " + str(penny)
		
		

	def MainFormLoad(self, sender, e):
		pass