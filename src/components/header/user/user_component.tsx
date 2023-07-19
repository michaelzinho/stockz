import style from './style.module.css'
import Link from 'next/link'
import Image from 'next/image';
import three_dots from '../../../../public/three_dots_icon.png'
import user_icon from '../../../../public/user_icon.png'
import { MoreVertical } from 'lucide-react'

export default function User_component () {

    return (
        <div className={style.user_component}>
            
            <MoreVertical width={35} height={35} color='#505050'/>
            <Link href="*">
                <Image className={style.user_image} src={user_icon} quality='100' alt="" width={60} height={60} />
            </Link>

        </div>
    )

}