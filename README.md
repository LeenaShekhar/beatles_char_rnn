Char-RNN Language Model to mimic lyrics by The Beatles & The Kinks
===

Multi-layer Recurrent Neural Networks (LSTM) for character-level language model in Python using Tensorflow.


## Requirements
- [Tensorflow 1.0](http://www.tensorflow.org)

## Basic Usage

1. Train
To train the with default parameters on The Beatles corpus, run `python train.py`. To read about all the parameters run `python train.py --help`.

2. Inference
To generate samples from a pre-rained model run, `python infer.py`. To read about all the parameters run `python infer.py --help`.

## Dataset

I used lyrics by two famous bands to train this model. 
1. The Beatles
2. The Kinks

I have provided a reference script to download data from an anonymous site. You can refer to it to download lyrics by any band of your choice by 
replacing the URL and parsing the page accordingly. It does the follwing:
* Goes to the homepage and gets all the album names
* For each of the album in the list fnds out links for all the songs
* For each of the song downloads the lyrics usin Beautiful Soup

You can find the raw data in `data/beatles_file.txt` and `kinks_file.txt` files. Merged data is under `data/input.txt` file. You can use `wc -l input.txt` to 
check the number of lines in the file. 

You can use any plain text file as input to train the model. If you have multiple .txt files you can concatenate them by using: 
`cat file1.txt file2.txt >> input.txt`


## Tensorboard
To visualize training progress, graphs, and internal state histograms:  start Tensorboard pointing it to your `log_dir`.  E.g.:
```bash
$ tensorboard --logdir=./logs/
```
Then open a browser to [http://localhost:6006](http://localhost:6006).
                       
![Alt text](plots/train_loss.png?raw=true "Training Loss for 50 epochs")                       

## What did the model learn
It is grea to know tat the model has successfully learnt the structure of a song, words mostly used in these lyris, and words which go along very well.
Below are the few examples generated by the model:

1. 
**Title:**    
got me life me    

**Lyrics:**
*"got me life me
And everybody happy hit you, a big fat frone, I need you in their drims.

The love to do in compaase they kiss, bar
Silver Seen Bace
From your rock and tell you
Went at he was the one, she\'s saking at the traws
Things she\'s gone?
Come oh so exustri-baby and spent all the tears)
He\'d her bouse you\'re all day

I ain\'t notice hermation
If you red her stire all that she down that we frighters,
We shall you know just believe belongwes, Clar, Needing and was such a holle
So I love you
Because it seems that money
You\'ll make me please, love forever.

Trushed to the cowbous to me
I\'ve got the lot in too late.

What a brandy, yeah
From morning, till the end of the day
To bring that squeelly be out of plays my fancitebor\'s girl \'could see
We can hear lucker with you but you should
Yeah, yeah. Reservaries I are weres,
And it can\'t stop them dreams."*

Hey, Mr...

Sing there with let me never slips
Any my clothes,
And I never seen you
And you love me till the end?
You always him on i

2.
**Title:**
Fordowsomplits Poppar

**Lyrics:**
"Hey, hey, why, do that it town.
Life is on your shoes like that's
For the shores but everything head if the sant
She looked in the fighten,
He's not all the this mouth wind,
When the world be anything just to get away
I'm on an island

This ship!)

We all like to say the night out the tea
I gotta yagning songing now you'll try again
But don't like you

Lew she floodight to say but I never let the brain.
It will quiet liteless bivind.
And I find it around,
With a Sunday They camble alary time.
No mailmed but you do.
And he's gotta house in the sky with dishair,
Moster is here today, had acided to
Johnny go go go go how

Won't you let is to know her
Got no where to smile.

They'll take are house,
Seems that life's a crazy of tea.

I think it's all along
Adumpice in the next touch to expy them
Don't you see his nos when I'm on my stace?
Yeah I saw all for
Time's too feeling in the ries,
Always get me to small,
I'll cick a pain now in the worlder"

3.
**Title:** 
gotta underneed

**Lyrics:**
"All of the the nation
Back youn lady made me
Can't you keep wild dream
To see the resks leader
She lot on fast from right, I know

Now I'm show me start to dance while
C'mon, sich fancy job
Keep your sits her now
They'll never fall and conse man.
Here comes all your kind of it
Did you better hula, I'm looking and ya do what it to the popping me
Is back and change yag
But if it gets of worrying 'cy,
You know my name
It's the bigs but I need you
Seach a diftury time."  

4.
**Title: My life with U.S**

**Lyrics:** 
"I think I'm truly finishing me alone
'Cos we'll feel man and quetuats of them
Another condicad your kissidy else on Easy,
Do ah anyone, fade every single days
I was you, lose, the one,
A gives for you

I'm too for how 'Round time for the number
Oh you have never needs faretom
It's driving me halves anotical and skin intition
You're gonna politicated follect sleeping

We live without look up the Nation.

Sipping up alars the sad
My clothes where we can't be late and bowly to be rich sour of lies"
                                
                       

## Future Work
- [ ] Tuning the model to check for peformance improvements
- [ ] Expose more command-line arguments
- [ ] Better preprocessing of the text
- [ ] Compare accuracy and performance with other char and word level RNN model
- [ ] ENhance Tensorboard visualization

## Contributing
Please feel free to:
* Leave feedback in the issues
* Open a Pull Request
* Share your success stories and data sets!

## Inspriration
* Inspired from Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).
* CS 20SI [stanford-tensorflow-tutorials] https://github.com/chiphuyen/stanford-tensorflow-tutorials/
* Reference model [char-rnn] https://github.com/sherjilozair/char-rnn-tensorflow
