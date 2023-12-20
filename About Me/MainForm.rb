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
		@label1.BackColor = System::Drawing::Color.DarkGreen
		@label1.Font = System::Drawing::Font.new("Century Gothic", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.White
		@label1.Location = System::Drawing::Point.new(153, 41)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(247, 114)
		@label1.TabIndex = 0
		@label1.Text = "My name is ''Sadie'', and I love the color green, cats, and video games!"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button1.Font = System::Drawing::Font.new("Century Gothic", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(145, 174)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(139, 49)
		@button1.TabIndex = 1
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button2.Font = System::Drawing::Font.new("Century Gothic", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(290, 174)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(128, 49)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Lime
		self.ClientSize = System::Drawing::Size.new(625, 410)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "About Me"
		self.ResumeLayout(false)
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = "My name is ''Sadie'', and I love the color green, cats, and video games!"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

