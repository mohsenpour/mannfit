import PongAIvAI
import math
Globalposofball = (220,140)

# team name: Abdelmegeed_elsafa7
# Names: Alaa Ahmed, Omar Baghdady
# Student ID's: 1002378884 , 1002087591





def get_gradient(previous_coordinates,ball_frect_pos):
    gradient = (ball_frect_pos[1] - previous_coordinates[1]) / (ball_frect_pos[0] - previous_coordinates[0])
    return gradient

def return_final_ypos(previous_coordinates,xpos,ball_frect_pos):
    gradient = get_gradient(previous_coordinates,ball_frect_pos)
    intersect = ball_frect_pos[1] - (gradient*ball_frect_pos[0])
    y = gradient*xpos + intersect
    return y



def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving

    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle.
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively

    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively

    The coordinates look as follows:

     0             x
     |------------->
     |
     |
     |
 y   v
    '''
    
    global Globalposofball

    
    if paddle_frect.pos[0] > other_paddle_frect.pos[0]:
        
        if ball_frect.pos[0] > Globalposofball[0]:#if it is going to the right
            
            
            y = return_final_ypos(Globalposofball,paddle_frect.pos[0],ball_frect.pos)
                
            if 0<=y<=table_size[1]:
               
                if paddle_frect.pos[1]+paddle_frect.size[1]/2< y:
                    
                    Globalposofball = ball_frect.pos  
                    return "down"
                else:
                    Globalposofball = ball_frect.pos 
                    return "up" 
              
                
                
            while y<0 or y > table_size[1]:
                if y>table_size[1] and y <= 2 * table_size[1]: #correct
                    y = y - table_size[1]
                    y = table_size[1] - y
                elif y>table_size[1] and y > 2 * table_size[1]:
                    number = ((y-table_size[1]) // table_size[1]) -1
                    y = (-number*table_size[1]) - (y%table_size[1])
                elif y<0  and y >= -table_size[1]: #correct
                    y = y+ 2*-y
                elif y<0  and y< -table_size[1]:#correct
                    number = (y // -table_size[1]) -1
                    y = table_size[1] + number*table_size[1] - (y % -table_size[1])
                    #check when it is exactly at sizes
             
   
                
                     
            if paddle_frect.pos[1]+paddle_frect.size[1]/2< y:
                Globalposofball = ball_frect.pos
                return "down"
            else:
                Globalposofball = ball_frect.pos
                return "up"     
   
        else:
            
            
            Globalposofball = ball_frect.pos
            if paddle_frect.pos[1]+paddle_frect.size[1]/2< table_size[1]/2:
            
                return "down"
            else:
               
                return "up"  
            
        
    else:
        
            if ball_frect.pos[0] < Globalposofball[0]:#if it is going to the right
                
                
                y = return_final_ypos(ball_frect.pos,paddle_frect.pos[0],Globalposofball)
                    
                if 0<=y<=table_size[1]:
                   
                    if paddle_frect.pos[1]+paddle_frect.size[1]/2< y:
                        
                        Globalposofball = ball_frect.pos  
                        return "down"
                    else:
                        Globalposofball = ball_frect.pos 
                        return "up" 
                  
                    
                    
                while y<0 or y > table_size[1]:
                    if y>table_size[1] and y <= 2 * table_size[1]: #correct
                        y = y - table_size[1]
                        y = table_size[1] - y
                    elif y>table_size[1] and y > 2 * table_size[1]:
                        number = ((y-table_size[1]) // table_size[1]) -1
                        y = (-number*table_size[1]) - (y%table_size[1])
                    elif y<0  and y >= -table_size[1]: #correct
                        y = y+ 2*-y
                    elif y<0  and y< -table_size[1]:#correct
                        number = (y // -table_size[1]) -1
                        y = table_size[1] + number*table_size[1] - (y % -table_size[1])
                        #check when it is exactly at sizes
                 
                     
        
                         
                if paddle_frect.pos[1]+paddle_frect.size[1]/2< y:
                    Globalposofball = ball_frect.pos
                    return "down"
                else:
                    Globalposofball = ball_frect.pos
                    return "up"     
       
            else:
                
                
                Globalposofball = ball_frect.pos
                if paddle_frect.pos[1]+paddle_frect.size[1]/2< table_size[1]/2:
                
                    return "down"
                else:
                   
                    return "up"  
     
        
        
    
