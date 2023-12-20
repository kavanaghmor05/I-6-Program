require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"


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
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(33, 24)
		@label1.TabIndex = 0
		@label1.Text = "A:"
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(12, 33)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(33, 23)
		@label2.TabIndex = 1
		@label2.Text = "B:"
		# 
		# label3
		# 
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 58)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(33, 22)
		@label3.TabIndex = 2
		@label3.Text = "C:"
		# 
		# label4
		# 
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 85)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(33, 28)
		@label4.TabIndex = 3
		@label4.Text = "D:"
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(51, 8)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 4
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(51, 34)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 20)
		@textBox2.TabIndex = 5
		@textBox2.TextChanged { |sender, e| self.TextBox2TextChanged(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(51, 60)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 20)
		@textBox3.TabIndex = 6
		@textBox3.TextChanged { |sender, e| self.TextBox3TextChanged(sender, e) }
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(51, 86)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 20)
		@textBox4.TabIndex = 7
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.FromArgb(192, 192, 255)
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(12, 136)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(113, 23)
		@label5.TabIndex = 8
		@label5.Text = "S:"
		@label5.Click { |sender, e| self.Label5Click(sender, e) }
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::Color.FromArgb(192, 192, 255)
		@label6.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(12, 159)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(113, 23)
		@label6.TabIndex = 9
		@label6.Text = "A:"
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.FromArgb(255, 255, 192)
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 199)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(113, 59)
		@button1.TabIndex = 10
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(255, 224, 192)
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(12, 264)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(113, 59)
		@button2.TabIndex = 11
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(12, 331)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(113, 59)
		@button3.TabIndex = 12
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(192, 255, 192)
		self.ClientSize = System::Drawing::Size.new(572, 426)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "prog52b"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button3Click(sender, e)
		Application.exit()
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@label5.Text = ""
		@label6.text = ""
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text)
		B = int(@textBox2.Text)
		C = int(@textBox3.Text)
		D = int(@textBox4.Text)
		S = A + B + C + D
	end
	
end

