'use client';

import style from './style.module.css'
import User_component from './user/user_component'
import Link from 'next/link'
import { usePathname, useRouter } from 'next/navigation'

function get_underline_name (link : string, link_to : string)
{

    const routname = usePathname()
    console.log(typeof routname, routname)

    if (link === "MENSAGENS") {

    }
    else if (link === "GALHERIA"){

    }
    else if (link === "/albuns"){
        let htmlString = '<u>MEUS ALBUNS</u>'
        return {__html :  htmlString}
    }
    else{
        return {__html :  link_to}
    }

}

export default function Header () {
    
    const routname = usePathname()
    console.log(typeof routname, routname)

    const MENSAGENS = '<u>MENSAGENS</u>'
    const GALHERIA = '<u>GALHERIA</u>'
    let MEUS_ALBUNS = '<p>MEUS ALBUNS</p>'

    return (
        <header className={style.header}>
            <Link href="home"> <h1>STOCKZ</h1> </Link> 

            <div className={style.nav}>
                <Link href="*"><p>MENSAGENS</p></Link>
                <Link href="*"><p>GALHERIA</p></Link>
                <Link href="albuns" >
                    <div dangerouslySetInnerHTML={get_underline_name(routname, '<p>MEUS ALBUNS</p>')}>

                    </div>
                </Link>
            
            </div>

            <div>
                <User_component/>
            </div>
        </header>
    )

}