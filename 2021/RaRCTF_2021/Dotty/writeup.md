# Writeup

exeファイルが与えられる。dnSpyでデコンパイルしたところ、次のようなコードが実行されていることが分かった。

```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace Dotty
{
	// Token: 0x02000002 RID: 2
	internal class Program
	{
		// Token: 0x06000002 RID: 2 RVA: 0x00002058 File Offset: 0x00000258
		private static string Dotter(string phrase)
		{
			return string.Join("|", from char c in phrase
			select Program.mapper[char.ToUpper(c)]);
		}

		// Token: 0x06000003 RID: 3 RVA: 0x0000208C File Offset: 0x0000028C
		private static void Main(string[] args)
		{
			Console.Write("Please enter your secret to encode: ");
			string phrase = Console.ReadLine();
			string text = Program.Dotter(phrase);
			if (text == Check.check)
			{
				Console.WriteLine("That's the right secret!");
			}
			else
			{
				Console.WriteLine(text);
			}
		}

		// Token: 0x04000001 RID: 1
		private static Dictionary<char, string> mapper = new Dictionary<char, string>
		{
			{
				' ',
				"/"
			},
			{
				'A',
				".-"
			},
			{
				'B',
				"-..."
			},
			{
				'C',
				"-.-."
			},
			{
				'D',
				"-.."
			},
			{
				'E',
				"."
			},
			{
				'F',
				"..-."
			},
			{
				'G',
				"--."
			},
			{
				'H',
				"...."
			},
			{
				'I',
				".."
			},
			{
				'J',
				".---"
			},
			{
				'K',
				"-.-"
			},
			{
				'L',
				".-.."
			},
			{
				'M',
				"--"
			},
			{
				'N',
				"-."
			},
			{
				'O',
				"---"
			},
			{
				'P',
				".--."
			},
			{
				'Q',
				"--.-"
			},
			{
				'R',
				".-."
			},
			{
				'S',
				"..."
			},
			{
				'T',
				"-"
			},
			{
				'U',
				"..-"
			},
			{
				'V',
				"...-"
			},
			{
				'W',
				".--"
			},
			{
				'X',
				"-..-"
			},
			{
				'Y',
				"-.--"
			},
			{
				'Z',
				"--.."
			},
			{
				'1',
				".----"
			},
			{
				'2',
				"..---"
			},
			{
				'3',
				"...--"
			},
			{
				'4',
				"....-"
			},
			{
				'5',
				"....."
			},
			{
				'6',
				"-...."
			},
			{
				'7',
				"--..."
			},
			{
				'8',
				"---.."
			},
			{
				'9',
				"----."
			},
			{
				'0',
				"-----"
			}
		};
	}
}

namespace Dotty
{
	// Token: 0x02000003 RID: 3
	internal class Check
	{
		// Token: 0x04000003 RID: 3
		public static string check = "-|....|.|/|..-.|.-..|.-|--.|/|..|...|/|---|.---|--.-|-..-|.|-.--|...--|..-|--|--..|.....|.--|..|--|.-..|.|.-..|.....|....-|-|.-|.....|-.-|--...|---|.-|--..|-|--.|..---|..---|--...|--.|-...|--..|..-.|-....|-.|.-..|--.-|.--.|.|--...|-|-....|.--.|--..|--...|.-..|.....|-|--.|-.-.|-.|-..|-...|--|--|...--|-..|.-|-.|.-..|.....|/|-...|.-|...|.|...--|..---";
	}
}
```

`check`を`mapper`から元に戻したところ、

```
THE FLAG IS OJQXEY3UMZ5WIMLEL54TA5K7OAZTG227GBZF6NLQPE7T6PZ7L5TGCNDBMM3DANL5 BASE32
```

というメッセージが得られた。指示通りBase32デコードすると、フラグが得られた。

```py
import base64

check = "-|....|.|/|..-.|.-..|.-|--.|/|..|...|/|---|.---|--.-|-..-|.|-.--|...--|..-|--|--..|.....|.--|..|--|.-..|.|.-..|.....|....-|-|.-|.....|-.-|--...|---|.-|--..|-|--.|..---|..---|--...|--.|-...|--..|..-.|-....|-.|.-..|--.-|.--.|.|--...|-|-....|.--.|--..|--...|.-..|.....|-|--.|-.-.|-.|-..|-...|--|--|...--|-..|.-|-.|.-..|.....|/|-...|.-|...|.|...--|..---"

d = {   
        ' ': "/" ,
		'A': ".-" ,
		'B': "-..." ,
		'C': "-.-." ,
		'D': "-.." ,
		'E': "." ,
		'F': "..-." ,
		'G': "--." ,
		'H': "...." ,
		'I': ".." ,
		'J': ".---" ,
		'K': "-.-" ,
		'L': ".-.." ,
		'M': "--" ,
		'N': "-." ,
		'O': "---" ,
		'P': ".--." ,
		'Q': "--.-" ,
		'R': ".-." ,
		'S': "..." ,
		'T': "-" ,
		'U': "..-" ,
		'V': "...-" ,
		'W': ".--" ,
		'X': "-..-" ,
		'Y': "-.--" ,
		'Z': "--.." ,
		'1': ".----" ,
		'2': "..---" ,
		'3': "...--" ,
		'4': "....-" ,
		'5': "....." ,
		'6': "-...." ,
		'7': "--..." ,
		'8': "---.." ,
		'9': "----." ,
		'0': "-----"
    }

d_swap = {v: k for k, v in d.items()}

msg = ''
for c in check.split('|'):
    msg += d_swap[c]
print(msg)
# THE FLAG IS OJQXEY3UMZ5WIMLEL54TA5K7OAZTG227GBZF6NLQPE7T6PZ7L5TGCNDBMM3DANL5 BASE32

flag = base64.b32decode('OJQXEY3UMZ5WIMLEL54TA5K7OAZTG227GBZF6NLQPE7T6PZ7L5TGCNDBMM3DANL5')
print(flag)
```

<!-- rarctf{d1d_y0u_p33k_0r_5py????_fa4ac605} -->
