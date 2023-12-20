require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label2 = System::Windows::Forms::Label.new()
		@button3 = System::Windows::Forms::Button.new()
		@button4 = System::Windows::Forms::Button.new()
		@label3 = System::Windows::Forms::Label.new()
		@button5 = System::Windows::Forms::Button.new()
		@button6 = System::Windows::Forms::Button.new()
		@label4 = System::Windows::Forms::Label.new()
		@button7 = System::Windows::Forms::Button.new()
		@button8 = System::Windows::Forms::Button.new()
		@label5 = System::Windows::Forms::Label.new()
		@button9 = System::Windows::Forms::Button.new()
		@button10 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.White
		@label1.Font = System::Drawing::Font.new("Old English Text MT", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(257, 29)
		@label1.TabIndex = 0
		@label1.Text = "1. Italian House - (609)-754-2226"
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Old English Text MT", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(275, 9)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Old English Text MT", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(356, 9)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.FromArgb(255, 255, 192)
		@label2.Font = System::Drawing::Font.new("Times New Roman", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(12, 38)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(303, 29)
		@label2.TabIndex = 3
		@label2.Text = "2. Hardvard Sentences - (858)-651-5050"
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Times New Roman", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(321, 38)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 23)
		@button3.TabIndex = 4
		@button3.Text = "Show"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# button4
		# 
		@button4.Font = System::Drawing::Font.new("Times New Roman", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button4.Location = System::Drawing::Point.new(402, 38)
		@button4.Name = "button4"
		@button4.Size = System::Drawing::Size.new(75, 23)
		@button4.TabIndex = 5
		@button4.Text = "Clear"
		@button4.UseVisualStyleBackColor = true
		@button4.Click { |sender, e| self.Button4Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.FromArgb(255, 128, 128)
		@label3.Font = System::Drawing::Font.new("Ravie", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 67)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(303, 29)
		@label3.TabIndex = 6
		@label3.Text = "3. Santa - 1-(603)-413-4124"
		# 
		# button5
		# 
		@button5.Font = System::Drawing::Font.new("Ravie", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button5.Location = System::Drawing::Point.new(308, 64)
		@button5.Name = "button5"
		@button5.Size = System::Drawing::Size.new(75, 23)
		@button5.TabIndex = 7
		@button5.Text = "Show"
		@button5.UseVisualStyleBackColor = true
		@button5.Click { |sender, e| self.Button5Click(sender, e) }
		# 
		# button6
		# 
		@button6.Font = System::Drawing::Font.new("Ravie", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button6.Location = System::Drawing::Point.new(389, 64)
		@button6.Name = "button6"
		@button6.Size = System::Drawing::Size.new(75, 23)
		@button6.TabIndex = 8
		@button6.Text = "Clear"
		@button6.UseVisualStyleBackColor = true
		@button6.Click { |sender, e| self.Button6Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.FromArgb(192, 192, 255)
		@label4.Font = System::Drawing::Font.new("Monotype Corsiva", 12, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 93)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(303, 29)
		@label4.TabIndex = 9
		@label4.Text = "4. Hogwarts Admissions - 605-475-6961"
		# 
		# button7
		# 
		@button7.Font = System::Drawing::Font.new("Monotype Corsiva", 8.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button7.Location = System::Drawing::Point.new(250, 92)
		@button7.Name = "button7"
		@button7.Size = System::Drawing::Size.new(75, 23)
		@button7.TabIndex = 10
		@button7.Text = "Show"
		@button7.UseVisualStyleBackColor = true
		@button7.Click { |sender, e| self.Button7Click(sender, e) }
		# 
		# button8
		# 
		@button8.Font = System::Drawing::Font.new("Monotype Corsiva", 8.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button8.Location = System::Drawing::Point.new(331, 93)
		@button8.Name = "button8"
		@button8.Size = System::Drawing::Size.new(75, 23)
		@button8.TabIndex = 11
		@button8.Text = "Clear"
		@button8.UseVisualStyleBackColor = true
		@button8.Click { |sender, e| self.Button8Click(sender, e) }
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.FromArgb(255, 192, 255)
		@label5.Font = System::Drawing::Font.new("Tempus Sans ITC", 12, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(12, 122)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(303, 29)
		@label5.TabIndex = 12
		@label5.Text = "5. Bad breath Hotline - (605)-475-6959"
		# 
		# button9
		# 
		@button9.Font = System::Drawing::Font.new("Tempus Sans ITC", 8.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button9.Location = System::Drawing::Point.new(297, 121)
		@button9.Name = "button9"
		@button9.Size = System::Drawing::Size.new(75, 23)
		@button9.TabIndex = 13
		@button9.Text = "Show"
		@button9.UseVisualStyleBackColor = true
		@button9.Click { |sender, e| self.Button9Click(sender, e) }
		# 
		# button10
		# 
		@button10.Font = System::Drawing::Font.new("Tempus Sans ITC", 8.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button10.Location = System::Drawing::Point.new(378, 122)
		@button10.Name = "button10"
		@button10.Size = System::Drawing::Size.new(75, 23)
		@button10.TabIndex = 14
		@button10.Text = "Clear"
		@button10.UseVisualStyleBackColor = true
		@button10.Click { |sender, e| self.Button10Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(192, 255, 192)
		self.ClientSize = System::Drawing::Size.new(671, 261)
		self.Controls.Add(@button10)
		self.Controls.Add(@button9)
		self.Controls.Add(@label5)
		self.Controls.Add(@button8)
		self.Controls.Add(@button7)
		self.Controls.Add(@label4)
		self.Controls.Add(@button6)
		self.Controls.Add(@button5)
		self.Controls.Add(@label3)
		self.Controls.Add(@button4)
		self.Controls.Add(@button3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Phonenumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "1. Italian House - (609)-754-2226"
		
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		
	end

	def Button3Click(sender, e)
		@label2.Text = "2. Harvard Sentences - (858)-651-5050"
		
	end

	def Button4Click(sender, e)
		@label2.Text = ""
		
	end

	def Button5Click(sender, e)
		@label3.Text = "3. Santa - 1-(603)-413-4124"
		
	end

	def Button6Click(sender, e)
		@label3.Text = ""
		
	end

	def Button7Click(sender, e)
		@label4.Text = "4. Hogwarts Admissions - 605-475-6961"
		
	end

	def Button8Click(sender, e)
		@label4.Text = ""
		
	end

	def Button9Click(sender, e)
		@label5.Text = "5. Bad breath Hotline - (605)-475-6959"
		
	end

	def Button10Click(sender, e)
		@label5.Text = ""
		
	end
end

