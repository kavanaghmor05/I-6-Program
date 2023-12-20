import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._score1 = System.Windows.Forms.Label()
		self._score2 = System.Windows.Forms.Label()
		self._score3 = System.Windows.Forms.Label()
		self._score4 = System.Windows.Forms.Label()
		self._score5 = System.Windows.Forms.Label()
		self._scorave = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._Calculate = System.Windows.Forms.Button()
		self._Clear = System.Windows.Forms.Button()
		self._Exit = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# score1
		# 
		self._score1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._score1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._score1.Location = System.Drawing.Point(12, 9)
		self._score1.Name = "score1"
		self._score1.Size = System.Drawing.Size(103, 30)
		self._score1.TabIndex = 0
		self._score1.Text = "Score 1:"
		# 
		# score2
		# 
		self._score2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._score2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._score2.Location = System.Drawing.Point(12, 39)
		self._score2.Name = "score2"
		self._score2.Size = System.Drawing.Size(103, 30)
		self._score2.TabIndex = 1
		self._score2.Text = "Score 2:"
		# 
		# score3
		# 
		self._score3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._score3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._score3.Location = System.Drawing.Point(12, 69)
		self._score3.Name = "score3"
		self._score3.Size = System.Drawing.Size(103, 30)
		self._score3.TabIndex = 2
		self._score3.Text = "Score 3:"
		# 
		# score4
		# 
		self._score4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._score4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._score4.Location = System.Drawing.Point(12, 99)
		self._score4.Name = "score4"
		self._score4.Size = System.Drawing.Size(103, 30)
		self._score4.TabIndex = 3
		self._score4.Text = "Score 4:"
		# 
		# score5
		# 
		self._score5.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._score5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._score5.Location = System.Drawing.Point(12, 129)
		self._score5.Name = "score5"
		self._score5.Size = System.Drawing.Size(103, 30)
		self._score5.TabIndex = 4
		self._score5.Text = "Score 5:"
		# 
		# scorave
		# 
		self._scorave.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._scorave.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._scorave.Location = System.Drawing.Point(12, 173)
		self._scorave.Name = "scorave"
		self._scorave.Size = System.Drawing.Size(383, 30)
		self._scorave.TabIndex = 5
		self._scorave.Text = "Score Average:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(121, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(152, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(121, 39)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(152, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(121, 69)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(152, 20)
		self._textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(121, 99)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(152, 20)
		self._textBox4.TabIndex = 9
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(121, 135)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(152, 20)
		self._textBox5.TabIndex = 10
		# 
		# Calculate
		# 
		self._Calculate.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._Calculate.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Calculate.Location = System.Drawing.Point(12, 206)
		self._Calculate.Name = "Calculate"
		self._Calculate.Size = System.Drawing.Size(110, 37)
		self._Calculate.TabIndex = 11
		self._Calculate.Text = "Calculate"
		self._Calculate.UseVisualStyleBackColor = False
		self._Calculate.Click += self.CalculateClick
		# 
		# Clear
		# 
		self._Clear.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._Clear.Cursor = System.Windows.Forms.Cursors.Default
		self._Clear.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Clear.ForeColor = System.Drawing.SystemColors.ControlText
		self._Clear.Location = System.Drawing.Point(149, 206)
		self._Clear.Name = "Clear"
		self._Clear.Size = System.Drawing.Size(110, 37)
		self._Clear.TabIndex = 12
		self._Clear.Text = "Clear"
		self._Clear.UseVisualStyleBackColor = False
		self._Clear.Click += self.ClearClick
		# 
		# Exit
		# 
		self._Exit.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._Exit.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Exit.Location = System.Drawing.Point(285, 206)
		self._Exit.Name = "Exit"
		self._Exit.Size = System.Drawing.Size(110, 37)
		self._Exit.TabIndex = 13
		self._Exit.Text = "Exit"
		self._Exit.UseVisualStyleBackColor = False
		self._Exit.Click += self.ExitClick
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 246)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(383, 30)
		self._label1.TabIndex = 14
		self._label1.Text = "Congrats! Great Job!"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(407, 287)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._Exit)
		self.Controls.Add(self._Clear)
		self.Controls.Add(self._Calculate)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._scorave)
		self.Controls.Add(self._score5)
		self.Controls.Add(self._score4)
		self.Controls.Add(self._score3)
		self.Controls.Add(self._score2)
		self.Controls.Add(self._score1)
		self.Name = "MainForm"
		self.Text = "pg198scoreaverage"
		self.ResumeLayout(False)
		self.PerformLayout()


	def ExitClick(self, sender, e):
		Application.Exit()

	def ClearClick(self, sender, e):
		self._scorave.Text = "Score Average:"
		self._textBox1.Items.Clear()
		self._textBox2.Items.Clear()
		self._textBox3.Items.Clear()
		self._textBox4.Items.Clear()
		self._textBox5.Items.Clear()

	def CalculateClick(self, sender, e):
		s1 = 0.0
		s2 = 0.0
		s3 = 0.0
		s4 = 0.0
		s5 = 0.0
		s1 = float(self._textBox1.Text)
		s2 = float(self._textBox2.Text)
		s3 = float(self._textBox3.Text)
		s4 = float(self._textBox4.Text)
		s5 = float(self._textBox5.Text)
		tosc = s1 + s2 + s3 + s4 + s5
		ave = tosc / 5
		self._scorave.Text = "Score Average: " + str(ave)
		if ave in range (95, 100+1):
			self._label1.Text = "Congrats! Gret Job!"
		else:
			self._label1.Text = ""