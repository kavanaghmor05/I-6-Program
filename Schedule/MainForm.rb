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
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Uighur", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(317, 386)
		@label1.TabIndex = 0
		@label1.Text = """1. Painting
2. Culinary 4A
3. Scifi and Fantasy
4. Choir
5. Animal Science
6. Computer Programming
7. Small Animal Care
8. Pre-Calc Honors"""
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button1.Font = System::Drawing::Font.new("Microsoft Uighur", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(335, 152)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(94, 42)
		@button1.TabIndex = 1
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(192, 192, 255)
		@button2.Font = System::Drawing::Font.new("Microsoft Uighur", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(435, 152)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(94, 42)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(192, 255, 192)
		self.ClientSize = System::Drawing::Size.new(750, 404)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end


	def Button1Click(sender, e)
		@label1.Text = "1. Painting\n2. Culinary 4A\n3. Scifi and Fantasy\n4. Choir\n5. Animal Science\n6. Computer Programming\n7. Small Animal Care\n8. Pre-Calc Honors"
		
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		
	end
end

