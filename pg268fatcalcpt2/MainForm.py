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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(548, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter total number of calories:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(267, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(283, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 48)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(560, 29)
		self._label2.TabIndex = 2
		self._label2.Text = "Enter total number of fat grams:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(280, 53)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(280, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(367, 29)
		self._label3.TabIndex = 4
		self._label3.Text = "% of calories that come from fat:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 147)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(124, 32)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(228, 147)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(124, 32)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(448, 147)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(124, 32)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(385, 115)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(187, 29)
		self._label6.TabIndex = 10
		self._label6.Text = "Is It Low Calorie?"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(581, 185)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg268FatCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._label3.Text = "% of calories that come from fat: "
		self._label6.Text = "Is It Low Calorie?"

	def Button1Click(self, sender, e):
		Cal = self._textBox1.Text
		Gram = self._textBox2.Text
		CalFat = Gram * 9
		P = CalFat /Cal
		PCF = P * 100
		self._label3.Text = "% of calories that come from fat: " + str(PCF) + "%"
		if Gram > Cal:
			self._label3.Text = "Error, grams and calories input incorrectly. Please try again."
		if PCF <= 30:
			self._label6.Text = "Is It Low Calorie? Yes!"