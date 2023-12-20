require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 12)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(28, 23)
		@label1.TabIndex = 0
		@label1.Text = "A:"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(12, 37)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(28, 23)
		@label2.TabIndex = 1
		@label2.Text = "B:"
		# 
		# label3
		# 
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 64)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(28, 23)
		@label3.TabIndex = 2
		@label3.Text = "C:"
		# 
		# label4
		# 
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 89)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(28, 23)
		@label4.TabIndex = 3
		@label4.Text = "D:"
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(46, 12)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(46, 38)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 20)
		@textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(46, 64)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 20)
		@textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(46, 90)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 20)
		@textBox4.TabIndex = 7
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.FromArgb(192, 255, 192)
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(19, 355)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(127, 65)
		@button1.TabIndex = 8
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(255, 255, 192)
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(226, 355)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(127, 65)
		@button2.TabIndex = 9
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(443, 355)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(127, 65)
		@button3.TabIndex = 10
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.FromArgb(255, 192, 255)
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(12, 138)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(238, 31)
		@label5.TabIndex = 11
		@label5.Text = "Sum:"
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::Color.FromArgb(255, 192, 255)
		@label6.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(12, 169)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(238, 31)
		@label6.TabIndex = 12
		@label6.Text = "Average:"
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(192, 192, 255)
		self.ClientSize = System::Drawing::Size.new(582, 432)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "prog52b2"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
	
	def int(text)     return text.to_i end
	def float(text)   return text.to_f end
	def str(text)     return text.to_s end
	def list(obj)     return obj.to_a  end
	def len(arr)      return arr.length end
	def input(msg="") print msg; return gets end
	def print(*args)  Kernel.print(*args, "\n") end
	def round(x, y)   return float((x * 10**y).round) / 10**y end
	def range(*args)  if len(args) == 1 then 
    	return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    	return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    	return  list((args[0]...args[1]).step(args[2])) end; end
	class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    	def random() return rand() end; 
    	def shuffle(arr) return arr.shuffle end; 
    	def choice(arr) return arr[randint(0, len(arr))] end; 
	end; $random = MyRandom.new(); $math = Math
	MessageBox = System::Windows::Forms::MessageBox
	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text)
		B = int(@textBox2.Text)
		C = int(@textBox3.Text)
		D = int(@textBox4.Text)
		S = A + B + C + D
		Ave = S/4.0
		@label5.Text = "Sum: " + str(S)
		@label6.Text = "Average: " + str(Ave)
	end

	def MainFormLoad(sender, e)
		
	end
end

