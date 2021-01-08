/*Panther ID: 5677483
 *COT 3530: Data Structures
 *Section: U01 (M & W 2:00pm)
 *Assignment #5
 */
package cop3530;
import java.io.*;
import java.lang.*;
import java.util.*;


public class KevinBaconGame {
	final int roles_sz = 3925000;
	final int movies_sz = 331500;
	HashMap <String,String[]> Actor2Movies;
	HashMap <String, ArrayList<String>>Movie2Actors;
	HashMap <String, Integer>BaconNum;
	Set<String> s;
    
    //constructor
    //the argument is the data file 
	public KevinBaconGame(String dataFileName) throws FileNotFoundException, IOException{
		try {
	         FileInputStream fileIn = new FileInputStream(dataFileName);
	         ObjectInputStream in = new ObjectInputStream(fileIn);
	         Actor2Movies = (HashMap <String,String[]>) in.readObject();
	         in.close();
	         fileIn.close();
	      }catch(IOException i) {
	         i.printStackTrace();
	         return;
	      }catch(ClassNotFoundException c) {
	         c.printStackTrace();
	         return;
	      }
		//create the Movie2actor hashmap 
		Movie2Actors = new HashMap <String, ArrayList<String>>();
		
		for(String actor : Actor2Movies.keySet()){
			for(String movie : Actor2Movies.get(actor)){
				//we search every movie for every actor
				if(!Movie2Actors.containsKey(movie)){
					//if the movie is not in the set of keys
					Movie2Actors.put(movie,  new ArrayList<String>());
					Movie2Actors.get(movie).ensureCapacity((int)(2* roles_sz / movies_sz));
				}
				Movie2Actors.get(movie).add(actor);
			}
		}
		for(String movie : Movie2Actors.keySet()){
			Movie2Actors.get(movie).trimToSize();
		}

	}
    
    
	//search bacon num of queryActor
	//this method return the bacon number
	public int getBaconNumber(String queryActor){
		
		//maintain queue Q of actors
		// maintain a set of movies to avoid looking at a movie twice
		BaconNum = new HashMap <String, Integer>();
		Queue<String> q = new ArrayDeque<String>();
		s = new HashSet<String>();
		if(!Actor2Movies.containsKey(queryActor)){
			System.out.println("actor not found");
			return -1;
		}
		//enqueue "Bacon, Kevin" and set his Bacon number to 0
		q.add("Bacon, Kevin");
		BaconNum.put("Bacon, Kevin",(Integer) 0);
		//while Q is not empty {
		while(q.size() > 0){
			//Remove actor from queue q
			String actor = q.poll();
			if (actor == null){
				return -15;
			}
			//for each movie m in which A has a role
			for(String movie : Actor2Movies.get(actor)){
				//if movie m has not already been looked at
				if(s.add(movie)){
					//for each actorB who appeared in movie{
					for(String actorB : Movie2Actors.get(movie)){
						//if actorB does not yet have a Bacon number
						if(!BaconNum.containsKey(actorB)){
							//set actorB's Bacon number to actor's Bacon number + 1
							int x = BaconNum.get(actor);
							BaconNum.put(actorB,(Integer)(x+1));
							//enqueue actorB
							q.add(actorB);
						}
						//if actorB is queryActor then return actorB's Bacon number
						if(actorB.equals(queryActor)){
							return BaconNum.get(actorB);
						}
					}
				}
			}
		}
		//if we get here then there was an error/we didn't find the actor
		return -2;
	}

}
