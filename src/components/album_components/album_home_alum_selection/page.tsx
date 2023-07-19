import style from './style.module.css'
import { Trash2, Move } from 'lucide-react'

export default function Album_chooose() {
  return (
    <div className={style.album}>
    <p>image</p>
    <div className={style.title}>
      <p>Album_name</p>
      <div className={style.icons}>
        <form action="">
          <button className={style.button} type="submit"><Trash2 className={style.trash} width={25} height={20} color='#767676'/></button>
        </form>
        
        <form action="">
          <button className={style.button} type="submit"><Move width={25} height={20} color='#767676'/></button>
        </form>
      </div>
    </div>
    </div> 
  )
}
