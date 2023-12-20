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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._Answer = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._operation = System.Windows.Forms.Label()
		self._Plusbutton = System.Windows.Forms.Button()
		self._Subbutton = System.Windows.Forms.Button()
		self._Multibutton = System.Windows.Forms.Button()
		self._Exbutton = System.Windows.Forms.Button()
		self._Divbutton = System.Windows.Forms.Button()
		self._Floorbutton = System.Windows.Forms.Button()
		self._Modbutton = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(142, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "First Number:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(39, 80)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(115, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Operation:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 138)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(173, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Second Number:"
		# 
		# Answer
		# 
		self._Answer.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._Answer.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Answer.Location = System.Drawing.Point(39, 188)
		self._Answer.Name = "Answer"
		self._Answer.Size = System.Drawing.Size(265, 23)
		self._Answer.TabIndex = 3
		self._Answer.Text = "Answer:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(160, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(144, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(191, 141)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(113, 20)
		self._textBox2.TabIndex = 5
		# 
		# operation
		# 
		self._operation.BackColor = System.Drawing.Color.White
		self._operation.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._operation.Location = System.Drawing.Point(160, 66)
		self._operation.Name = "operation"
		self._operation.Size = System.Drawing.Size(135, 52)
		self._operation.TabIndex = 6
		self._operation.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Plusbutton
		# 
		self._Plusbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Plusbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Plusbutton.Location = System.Drawing.Point(328, 9)
		self._Plusbutton.Name = "Plusbutton"
		self._Plusbutton.Size = System.Drawing.Size(88, 38)
		self._Plusbutton.TabIndex = 7
		self._Plusbutton.Text = "+"
		self._Plusbutton.UseVisualStyleBackColor = False
		self._Plusbutton.Click += self.PlusbuttonClick
		# 
		# Subbutton
		# 
		self._Subbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Subbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Subbutton.Location = System.Drawing.Point(422, 9)
		self._Subbutton.Name = "Subbutton"
		self._Subbutton.Size = System.Drawing.Size(88, 38)
		self._Subbutton.TabIndex = 8
		self._Subbutton.Text = "-"
		self._Subbutton.UseVisualStyleBackColor = False
		self._Subbutton.Click += self.SubbuttonClick
		# 
		# Multibutton
		# 
		self._Multibutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Multibutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Multibutton.Location = System.Drawing.Point(516, 9)
		self._Multibutton.Name = "Multibutton"
		self._Multibutton.Size = System.Drawing.Size(88, 38)
		self._Multibutton.TabIndex = 9
		self._Multibutton.Text = "X"
		self._Multibutton.UseVisualStyleBackColor = False
		self._Multibutton.Click += self.MultibuttonClick
		# 
		# Exbutton
		# 
		self._Exbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Exbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Exbutton.Location = System.Drawing.Point(328, 50)
		self._Exbutton.Name = "Exbutton"
		self._Exbutton.Size = System.Drawing.Size(88, 38)
		self._Exbutton.TabIndex = 10
		self._Exbutton.Text = "^"
		self._Exbutton.UseVisualStyleBackColor = False
		self._Exbutton.Click += self.ExbuttonClick
		# 
		# Divbutton
		# 
		self._Divbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Divbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Divbutton.Location = System.Drawing.Point(422, 50)
		self._Divbutton.Name = "Divbutton"
		self._Divbutton.Size = System.Drawing.Size(88, 38)
		self._Divbutton.TabIndex = 11
		self._Divbutton.Text = "/"
		self._Divbutton.UseVisualStyleBackColor = False
		self._Divbutton.Click += self.DivbuttonClick
		# 
		# Floorbutton
		# 
		self._Floorbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Floorbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Floorbutton.Location = System.Drawing.Point(516, 50)
		self._Floorbutton.Name = "Floorbutton"
		self._Floorbutton.Size = System.Drawing.Size(88, 38)
		self._Floorbutton.TabIndex = 12
		self._Floorbutton.Text = "//"
		self._Floorbutton.UseVisualStyleBackColor = False
		self._Floorbutton.Click += self.FloorbuttonClick
		# 
		# Modbutton
		# 
		self._Modbutton.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Modbutton.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Modbutton.Location = System.Drawing.Point(422, 94)
		self._Modbutton.Name = "Modbutton"
		self._Modbutton.Size = System.Drawing.Size(88, 38)
		self._Modbutton.TabIndex = 13
		self._Modbutton.Text = "Mod"
		self._Modbutton.UseVisualStyleBackColor = False
		self._Modbutton.Click += self.ModbuttonClick
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(422, 138)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(88, 38)
		self._button8.TabIndex = 14
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(422, 182)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(88, 38)
		self._button9.TabIndex = 15
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(612, 229)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._Modbutton)
		self.Controls.Add(self._Floorbutton)
		self.Controls.Add(self._Divbutton)
		self.Controls.Add(self._Exbutton)
		self.Controls.Add(self._Multibutton)
		self.Controls.Add(self._Subbutton)
		self.Controls.Add(self._Plusbutton)
		self.Controls.Add(self._operation)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._Answer)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg140simplecalc"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button9Click(self, sender, e):
		Application.Exit()

	def Button8Click(self, sender, e):
		self._textBox1.Items.Clear()
		self._textBox2.Items.Clear()
		self._operation.Text = ""
		self._Answer.Text = "Answer: "

	def PlusbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "+"
		Answer = float(self._textBox1.Text) + float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)

	def SubbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "-"
		Answer = float(self._textBox1.Text) - float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)
		

	def MultibuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "X"
		Answer = float(self._textBox1.Text) * float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)

	def ExbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "^"
		Answer = float(self._textBox1.Text) ** float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)

	def DivbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "/"
		Answer = float(self._textBox1.Text) / float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)

	def FloorbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "//"
		Answer = float(self._textBox1.Text) // float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)

	def ModbuttonClick(self, sender, e):
		Answer = 0.0
		self._operation.Text = "%"
		Answer = float(self._textBox1.Text) % float(self._textBox2.Text)
		self._Answer.Text = "Answer: " + str(Answer)